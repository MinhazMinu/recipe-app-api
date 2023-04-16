###### Require email input

-   As usel lets first create the tests for this
-   in test_models.py create a new method test_new_user_without_email_raise_error()

```py
def test_new_user_without_email_raise_error(self):
        """Test creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Testpass123")
```

> The with statement in Python is used for resource management and exception handling to make the code cleaner and much more readable.

-   run the test & it will pass because we have this line in our create_user class

-   Now Lets implement this.
