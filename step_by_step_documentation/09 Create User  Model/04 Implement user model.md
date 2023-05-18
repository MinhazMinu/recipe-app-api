###### Implement user model

-   in models.py we add

```py
"""
Database Models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# manage for user model
class UserManager(BaseUserManager):
    """manager for users."""

    # method for create a user
    def create_user(self, email, password=None, **extra_fields):
        """Create and save and return a  new user."""
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

# User model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
```

-   In settings.py we add

```py
AUTH_USER_MODEL = "core.User"
```

-   Now create a migration file

```sh
docker-compose run --rm app sh -c "python manage.py makemigrations"
```

-   now we need to do a fresh migration

    -   docker-compose down
    -   docker volume ls
    -   docker volume rm name_of_the_volume
    -   docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

-   Now we can chekck out test

```sh
docker-compose run --rm app sh -c "python manage.py test"
```
