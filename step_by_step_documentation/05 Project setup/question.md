Q1. How docker-compose.yml is sure that it is building the docker image from the Dockerfile in the current directory?

> docker-compose.yml file has a build context which is set to current directory. So it will look for Dockerfile in the current directory.

Q2. How to run multiple docker containers at once?

> docker-compose up
> Q3. Example of docker-compose.yml file for multiple containers?
>
> ```yml
> version: "3.9"
>
> services:
>     python:
>         build: ./python
>         ports:
>             - "8000:8000"
>
>     php:
>         build: ./php
>         ports:
>             - "8001:8001"
> ```

Q3. What is the difference between docker-compose up and docker-compose up --build?

> docker-compose up --build will build the image before running the container. docker-compose up will use the existing image.
