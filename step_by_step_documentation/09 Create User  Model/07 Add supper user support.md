###### Add super user support

-   Lets create the test first
-   In test_models.py

```py
def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com", "Testpass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
```

-   now run test. It will fails as we don not implement create_superuser in UserManager

> **warning**
> AttributeError: 'UserManager' object has no attribute 'create_superuser'

-   in models.py

```py
def create_superuser(self, email, password):
        """Create and save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
```

And now rub test again
