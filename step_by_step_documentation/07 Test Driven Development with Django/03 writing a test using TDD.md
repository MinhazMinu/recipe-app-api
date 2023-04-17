###### Writing a test using TDD

We first create the test then add functionality to pass the test

-   In tests.py we will write our test case first

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

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted"""
        self.assertEqual(calc.subtract(8, 3), 5)
```

if we run this now using

```sh
docker-compose run --rm app sh -c "python manage.py test"
```

we will see an error in test cases

-   Now add functionality in calc.py to pass the test

```py
"""
Calculator Function
"""


def add(x, y):
    """Add x and y return result."""
    return x + y


def subtract(x, y):
    """Subtract x and y return result."""
    return x - y
```
