###### Implement create user api

-   First create a serializers.py file inside user
    > serializer converts JSON to python object and vice-versa

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

-   in views.py file

```py
"""Views for the user API"""

from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer
```

> generics is a module in Django REST framework that provides generic class-based views for common use cases. These views are pre-configured to handle common tasks such as retrieving a list of objects, creating new objects, and updating existing objects.

> The generics module includes a set of base views that can be extended to build custom views for specific use cases. These base views include:
> **_ListAPIView_**: A view for retrieving a list of objects.
> **_CreateAPIView_**: A view for creating a new object.
> **_RetrieveAPIView_**: A view for retrieving a single object by ID.
> **_UpdateAPIView_**: A view for updating an existing object by ID.
> **_DestroyAPIView_**: A view for deleting an object by ID.

> By using these generic views, you can reduce the amount of boilerplate code needed to create views for your API.

-   Now we need to configure our url \* Create a urls.py inside user directory

        ```py
        """URL mapping for the user API"""
        from django.urls import path
        from user import views
        app_name = "user"

        urlpatterns = [
        path("create/", views.CreateUserView.as_view(), name="create"),
        ]
        ```

*   Add this url path to main app url

```py
        from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularSwaggerView,

    )
    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
        path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
        ),
        path("api/user/", include("user.urls")),
    ]

```
* Now test
```sh
docker-compose run --rm app sh -c "python manage.py test"
```