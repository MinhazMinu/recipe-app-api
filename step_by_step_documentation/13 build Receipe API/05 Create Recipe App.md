###### Create Recipe App

-   Lets create a recipe app where we write all our code for recipe endpoints.

```sh
docker-compose run --rm app sh -c "python manage.py startapp recipe"
```

-   Remove unwanted folder and files

    -   migrations
    -   tests.py
    -   admin.py
    -   models.py

-   in settings.py add recipe app to INSTALLED_APPS

```py
INSTALLED_APPS = [
    ...
    'recipe',
]
```
