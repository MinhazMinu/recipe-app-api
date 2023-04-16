###### Add user model test

-   Create a test_models.py inside tests directory

```py
"""
Tests for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

# define class for test model
class ModelTests(TestCase):
    # define method for to test if a user is created successfully using email
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "user@example.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
```

now we can check tet using

```sh
docker-compose run --rm app sh -c "python manage.py test"
```
