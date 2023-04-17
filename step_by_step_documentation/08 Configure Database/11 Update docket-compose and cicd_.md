#### Update Docker Compose and CICD

-   In docker-compose.yml file

```yml
command: >
    sh -c "python manage.py wait_for_db &&
            python manage.py migrate &&
            python manage.py runserver 0.0.0.0:8000"
```

and in checks.yml file

```yml
- name: Test
    run: docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test"
```

-   Now run

```sh
docker-compose down

docker-compose up
```
