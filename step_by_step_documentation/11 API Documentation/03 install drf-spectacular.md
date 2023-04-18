###### Install drf-spectacular

-   In requirement.txt

```
Django>=3.2.4,<3.3
djangorestframework>=3.12.4,<3.13
psycopg2>=2.8.6,<2.9
drf-spectacular>=0.15.1,<0.16
```

-   now rebuild docker container

```sh
docker-compose build
```

-   in settings.py, INSTALLED_APP

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
    "drf-spectacular",
]
```

And in the bottom of the settings.py we will add

```py
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```
