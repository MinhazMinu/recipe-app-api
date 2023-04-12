###### Writing a test

-   Temporary basis we create calc.py inside app directory

```py
"""
Calculator Function
"""


def add(x, y):
    """Add x and y return result."""
    return x + y
```

-   create a tests.py in the app directory

```py
"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(calc.add(3, 8), 11)
```

-   Now run bellow command

```sh
docker-compose run --rm app sh -c "python manage.py test"
```
