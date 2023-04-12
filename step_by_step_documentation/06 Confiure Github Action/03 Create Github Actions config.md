###### Create github actions

-   Create a .github folder in root directory
-   Create workflows folder inside github folder
-   inside workflow folder create checks.yml file

```yml
---
name: Checks

# action will trigger at git hub push
on: [push]

# which jobs it will run
jobs:
    test-lint:
        name: Test and test-lint
        # which os it will run inside docker container
        runs-on: ubuntu-20.04
        # a job may need multiple step to complete
        steps:
            - name: Login to Docker Hub
              uses: docker/login-action@v1
              with:
                  username: ${{ secrets.DOCKERHUB_USER }}
                  password: ${{ secrets.DOCKERHUB_TOKEN }}
            - name: Checkout
              uses: actions/checkout@v3
            - name: Test
              run: docker-compose run --rm app sh -c "python manage.py test"
            - name: Lint
              run: docker-compose run --rm app sh -c "flake8"
```
