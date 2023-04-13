###### Database configuration with Django

-   Configure Django
    -   Tell Django how to connect
-   Install database adaptor dependencies
    -   Install the tool Django uses to connect
-   Update Python requirements

    -   To require postgres django adaptor

-   Before connection Django needs to know the following....
    -   Engine (type of database)
    -   Hostname (Ip or domain name of database)
    -   Port number (default: 5432)
    -   Database name
    -   Username
    -   Password

All this are already define in django \*settings.py\*

###### Environment variable

-   We will pull config values from environment variables
-   Can be easily passed to docker
-   Used in local dev or prod
-   This means its a single place to configure project

*   we can pull environment variable using python by

```py
OS.environ.get('DB_HOST')
```

###### Psycopg2

-   The package we need in order for Django to connect to our database
-   Most popular PostgreSQL adaptor for python

*   Installation options
    -   psycopg2-binary
        -   OK for local development
        -   Not good for production
    -   pscopg2
        -   Compiles from source
        -   require Additional dependencies
        -   Easy to install with Docker
        -   we will use it

###### Installing Psycopg2

-   List of package dependencies in docs
    -   C compiler
    -   python3-dev
    -   libpq-dev
* This packages name is not same in Alpine 
    * Equivalent packages name
        * postgresql-client
        * build-base
        * postgresql-dev
        * musl-dev

###### Docker best practice:
* Clean up build dependencies
    * build-base
    * postgresql-dev
    * musl-dev
This packages are only use to install the postgreSQl. Not for running.

