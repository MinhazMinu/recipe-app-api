###### Create Project Docker file

-   create a Docker file inside root directory.

```docker
FROM python:3.9-alpine3.13
LABEL maintainer="Minhaz:minhaz.taher@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser  \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
```

###### Create .dockerignore file in root directory

```
.git
.gitignore
.docker
app/__pycache__/
app/*/__pycache__/
app/*/*/__pycache__/
app/*/*/*/__pycache__/
.env
.venv
venv/
```

###### Run docker build command. it will create an image

```sh
docker build .
```
