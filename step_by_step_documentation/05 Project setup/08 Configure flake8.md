###### Configure flake8.md

-   create a requirements.dev.txt file in root directory
```
flake8>=3.9.2,<3.10
```
-   add below code to docker-compose.yml file

```docker
args:
    - DEV=true
```

So file now look like this.

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
            sh -c "python manage.py runserver 0.0.0.0"
```

-   add _COPY ./requirements.dev.txt /tmp/requirements.dev.txt_ in the Dockerfile

```docker
FROM python:3.9-alpine3.13
LABEL maintainer="Minhaz:minhaz.taher@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ] ; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser  \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
```

Here _ARG DEV=false_ which is overwrite from docker-compose file, so that by default it is not running in development mode.

we check _if [ "$DEV" = "true" ]_, so if dev is true than it will copy the requirements.dev.txt file

-   rebuild the docker image

```sh
docker-compose build
```

###### .flake8 configuration file

-   inside app directory create a .flake& file

```
[flake8]
exclude =
    migrations,
    __pycache__,
    manage.py,
    settings.py,
```

-   to run linting

```sh
docker-compose run --rm app sh -c "flake8"
```
