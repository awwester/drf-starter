# Summary
This is a starter project that is a great place to start handling a lot of the boilerplate of starting a new API project.

# Features
- Docker
- Django
- Django Rest Framework
- Authentication endpoints

# Install
The only system requisites are docker and docker-compose, everything else is handled inside the docker container.

1) `make setup` (or run the setup commands in Makefile if you don't have make installed.)
2) `docker-compose up`
3) `docker-compose exec django ./manage.py migrate`

# Usage

##### Running django commands
Since the project is running in a docker container you can run django commands
with `docker-compose exec django ./manage.py <command>`.

##### Running tests
You can run tests with `make test` or run with extra options using a docker-compose exec script.

##### Owning files
When generating new files through `startapp` or `makemigrations` for instance, the files will not be owned by you and you won't have permission to modify. You can fix that by running `make chown`.
