###### Configure Database in Django

-   On settings.py go to DATABASES

```py
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),

        # this have to be same as environment variable set in docker-compose.yml file
    }
}
```

-   now we can remove sqllite3 database from out project file
