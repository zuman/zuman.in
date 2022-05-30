# zuman.one
Source code to my personal website !

[zuman.one](https://zuman.one)

## Setup notes:
### 1. Create a **.env** file in **root** directory similar to the one mentioned below.

>**.env**
```
SECRET_KEY=...
SALT=...
LOG_LEVEL=...
#DEBUG, INFO, WARNING, ERROR, CRITICAL

SQLALCHEMY_DATABASE_URI=...
POSTGRES_PASSWORD=...

SESSION_TYPE=memcached
SESSION_MEMCACHED=memcached:11211
SESSION_COOKIE_NAME=...
SESSION_COOKIE_SECURE=False
# True for production
PERMANENT_SESSION_LIFETIME=86400
# Any integer to denote seconds

REMEMBER_COOKIE_DURATION=2592000
# Any integer to denote seconds
REMEMBER_COOKIE_HTTPONLY=True
REMEMBER_COOKIE_SECURE=False
# True for production

MAIL_USERNAME=...
MAIL_PASSWORD=...

FLASK_APP=main.py
FLASK_ENV=...
FLASK_DEBUG=...
# 0 for production, 1 for development
```

### 2. Create an external network
```
docker network create --attachable proxy-network
```

### 3. Build image and run docker compose

```
docker build api -t api
sudo rm -rf db/migrations/
sudo rm -rf db/data/
export POSTGRES_PASSWORD=... # from .env
docker compose up -d
```

### 4. Initialize the database

```
docker exec -it zumanin-zuman-api-1 sh /app/db-sync
```