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

> This is a sample Django test case for testing a custom user model's create_user method.

> The test case inherits from TestCase, which is a class provided by Django for writing test cases.

> The test_create_user_with_email_successful method tests if a user is created successfully using an email and password.

> The method first defines email and password variables to use as arguments when creating a new user.

> Then it calls the create_user method on the custom user model using get_user_model() to get the user model for the current project.

> The method then asserts that the user's email is equal to the email variable, and that the password can be checked using the check_password method on the user object.

> This test case is a good starting point for testing the user model's functionality. It can be expanded upon to cover additional scenarios, such as testing the create_superuser method or testing invalid email and password inputs.

now we can check test using

```sh
docker-compose run --rm app sh -c "python manage.py test"
```
