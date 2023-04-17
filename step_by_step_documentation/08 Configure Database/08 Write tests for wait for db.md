###### wait_for_db (tests)

-   Create below folder and file

    -   app\core\management\commands\wait_for_db.py
    -   inside commands directory create \_\_init\_\_.py
    -   inside management directory create \_\_init\_\_.py
    -   app\core\tests\tests_commands.py
    -   inside tests directory create \_\_init\_\_.py

-   In tests_command

```py
"""
Test custom Django management command to pause execution until database is available
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test command"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available"""
        patched_check.return_value = True
        call_command("wait_for_db")
        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting OperationalError"""
        patched_check.side_effect = (
            [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        )

        call_command("wait_for_db")
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=["default"])
```

> This code defines a unit test to test a custom Django management command called wait_for_db. This command is intended to pause execution until the database is available for connection. The unit test uses the SimpleTestCase class from Django's testing framework.

> The @patch decorator is used to mock the check method of the wait_for_db command. The patched_check argument in the test_wait_for_db_ready and test_wait_for_db_delay methods represents the mocked version of the check method.

> In the test_wait_for_db_ready method, the patched_check method is mocked to return True, indicating that the database is available. Then, the call_command function is called to execute the wait_for_db command. Finally, the assert_called_once_with method is used to check that the check method was called once with the databases parameter set to ["default"].

> In the test_wait_for_db_delay method, the patched_check method is mocked to raise an OperationalError exception on the first two calls, then raise a Psycopg2Error exception on the next three calls, and finally return True on the sixth call. This simulates a delay in connecting to the database. The patched_sleep argument is used to mock the time.sleep function, which is called between retries. Again, the call_command function is used to execute the wait_for_db command. Finally, the assert_called_with method is used to check that the check method was called six times with the databases parameter set to ["default"]. Additionally, the assertEqual method is used to check that the call_count attribute of patched_check is equal to 6.

-   And in wait_for_db.py

```py
"""
Django Command to wait for the database to be available
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        pass
```

we do not implemented this command yet. so if we run

```sh
docker-compose run --rm app sh -c "python manage.py test"
```

we can see two test case fail
