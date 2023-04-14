###### wait_for_db (tests)

-   Create below folder and file

    -   app\core\management\commands\wait_for_db.py
    -   inside commands directory create \_\_init\_\_.py
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
        patched_check.assert_called_once_with(database=["default"])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting OperationalError"""
        patched_check.side_effect = (
            [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        )

        call_command("wait_for_db")
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(database=["default"])
```

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

we do not implemented thsi command yet. so if we run

```sh
docker-compose run --rm app sh -c "python manage.py test"
```

we can see two test case fail
