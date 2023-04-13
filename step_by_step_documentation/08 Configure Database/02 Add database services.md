###### Add database services to docker-compose

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
        # Set environment variable to use. These are same as db environment
        environment:
            - DB_HOST=db
            - DB_NAME=devdb
            - DB_USER=devuser
            - DB_PASSWORD=changeme
        # this means App service f=depends on db service
        depends_on:
            - db

    db:
        image: postgres:13-alpine
        volumes:
            - dev-db-data:/var/lib/postgresql/data
        environment:
            - POSTGRES_USER=devuser
            - POSTGRES_PASSWORD=changeme
            - POSTGRES_DB=devdb

volumes:
    dev-db-data:
```
