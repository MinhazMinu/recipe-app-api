###### Run project with docker compose

```
docker-compose up
```

For some reason i need to change my docker-compose.yml file like thsi

```yml
version: "3.9"

services:
    app:
        build:
            context: .
            args:
                - DEV=true
        ports:
            - "8000:8000"
        volumes:
            - ./app:/app
        command: >
            sh -c "python manage.py runserver 0.0.0.0:8000"
```

made a change in here _sh -c "python manage.py runserver 0.0.0.0:8000"_

-   now after running docker-compose up, in browser visit 127.0.0.1:8000

*   ctrl+ c to stope the service
