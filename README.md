# Klinify Backend Task

## Description

The project is made upon Docker with Django, Python and Postgres. 
The project uses JWT for authentication.

## Prerequisite

1. Docker installed
2. Python3.6

## How to run the project

1. Clone the project and Goto base directory klinify, Build the docker image.

```
* docker-compose build
```

2. Start the servers.

```
* docker-compose up
```

3. Do the migrations.

```
docker-compose run web /usr/local/bin/python manage.py makemigrations

docker-compose run web /usr/local/bin/python manage.py migrate
```

4. The project is up and running. Postman collection is given in the repository to try the api.


## Replay Attacks prevention.

Replay attacks can be only prevented by storing blacklisted tokens in a db or an in memory database like redis(to make the lookup lot faster). The tradeoff is the JWT does not remain stateless on applying the blacklist check. The Blacklist on the redis can be asynchronously updated using celery at backend i.e celery checks every 5 minute which of the tokens has expired and need not to be in the database.
