###### Create Docker Compose Configuration

-   In root directory create a docker-compose.yml file

```yml
# version of docker compose syntax
version: "3.9"

#services that are need for the application
services:
    #app is the name of our service
    app:
        # this means we want to build the dockerfile inside current directory
        build:
            context: .
        # this is the port mapping
        # this maps local machine 8000 port to docker container 8000 port
        ports:
            - "8000:8000"
        # volumes are way of mapping directory to our system to docker container
        # reason is , if we update our project to local container  it will reflect in the container real time
        volumes:
            - ./app:/app
        # command that will used to run the service
        command: >
            sh -c "python manage.py runserver 0.0.0.0"
```

-   run docker compose build command

```sh
docker-compose build
```

Dockerfile VS docker-compose.yml

-   Dockerfile is used to build a docker image
-   docker-compose.yml is used to build a docker container

> The key difference between the Dockerfile and docker-compose is that the Dockerfile describes how to build Docker images, while docker-compose is used to run Docker containers.

> The contents of a Dockerfile describe how to create and build a Docker image, while docker-compose is a command that runs Docker containers based on settings described in a docker-compose.yaml file.

docker image vs docker container

-   Docker image is a template that contains the instructions for creating a Docker container.
-   Docker container is a running instance of a Docker image.
