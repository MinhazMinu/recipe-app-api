1. What is get_user_model and how its know which model to use?

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

2. UserManager class ta ki ? keno use kora hoy?

```py
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

    # method for create a user
    def create_superuser(self, email, password):
        """Create and save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
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

3. ekahane auto user vreate hocchek ivabe.. kew to setUp method re call kore nai keno? reverse() method kissu buji nai;

```py
""" Test for django admin modification"""

from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test for Django admin site"""
    # set up client and user which will be needed for every test case
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com", password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="password123",
            name="Test user",  # noqa
        )

    # test user list
    def test_users_lists(self):
        """Test that users are listed on user page"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
"""
```

4. SpectacularSwaggerView.as_view

```py
in urls.py file
# import these modules
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # add this two path
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]
```

5. Serializer

```py
"""Serializers for the user app."""

from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user model."""

    class Meta:
        """Meta class for the user serializer."""

        model = get_user_model()
        fields = ("email", "password", "name")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it."""
        return get_user_model().objects.create_user(**validated_data)
```

5. generics

```py
   """Views for the user API"""


from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
"""Create a new user in the system."""

    serializer_class = UserSerializer

```
