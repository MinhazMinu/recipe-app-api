###### Implement token api

-   authtoken comes with django rest framework but its a seperate app. so we need to add this in istalled apps in settings.py
-   add 'rest_framework.authtoken' in installed apps

```py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "user",
]
```

-   we will create a new serializer for token api in serializers.py

```py
class AuthTokenSerializer:
    """Serializer for the user authentication object."""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,  # noqa
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return attrs
```

-   now lets crest a view for token api in views.py

```py
class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
```

* Add the url for this view in urls.py

```py
