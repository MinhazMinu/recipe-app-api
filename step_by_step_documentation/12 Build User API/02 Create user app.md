###### Create user app

-   Lets create a new app called user

```sh
docker-compose run --rm app sh -c "python manage.py startapp user"
```

-   now we can remove some file which we dont need

    -   migration.py : we keep all our migration file in core app
    -   admin.py : we keep all our admin file in core app
    -   models.py : we keep all our models file in core app
    -   test.py : we will create a test directory to write our test

-   create test directory
    -   create a test directory inside user app
    -   create a \_\_init\_\_.py inside test directory

*   Now add this new user app in settings.py

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
    "drf_spectacular",
    "user",
]
```
