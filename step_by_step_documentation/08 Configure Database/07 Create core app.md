###### Create Core App

-   We need to create an app named _core_

```sh
docker-compose run --rm app sh -c "python manage.py startapp core"
```

-   We don`t need tests.py and views.py, so can delete them

*   Create a tests folder. inside tests folder create \_\_init.py\_\_
*   settings.py file we need to add core in _INSTALLED_APPS_
