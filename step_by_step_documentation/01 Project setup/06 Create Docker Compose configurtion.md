###### Create Docker Compose Configuration

-   In root directory create a docker-compose.yml file

```yml
# version of docker compose syntext
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

```
docker-compose build
```
