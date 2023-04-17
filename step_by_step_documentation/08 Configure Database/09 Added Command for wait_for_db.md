###### Added command for wait_for_db

-   wait_for_db.py

```py
"""
Django Command to wait for the database to be available
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Entry point for command execution"""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
```

> This is a custom Django management command called wait_for_db which is intended to pause execution until the database is available for connection.

> The command extends the BaseCommand class provided by Django's command framework. The handle method is the entry point for command execution and is responsible for implementing the command's functionality.

> The handle method starts by printing a message to the console indicating that it is waiting for the database. Then it sets a flag db_up to False, indicating that the database is not yet available.

> It then enters a loop that repeatedly tries to connect to the database by calling the check method. The check method verifies that the database is available for connection. If an exception of type Psycopg2Error or OperationalError is raised during this process, it indicates that the database is not yet available. In this case, the loop waits for one second by calling the time.sleep function and then tries again.

> When the check method succeeds in connecting to the database, it sets db_up to True and the loop ends. Finally, a message is printed to the console indicating that the database is available.

> This command can be executed from the command line using the python manage.py wait_for_db command. It is commonly used in Docker containers to delay the start of a service until the database is available.

-   for flake8 warning we can use

```
# noqa
```
