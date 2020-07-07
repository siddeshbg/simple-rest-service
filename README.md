# vowel-count-rest-api

This project demonstrates a simple rest service built using the Django REST
Framework (DRF).

## Introduction
At the high level, this project will provide an API like
 
```http://127.0.0.1:8000/api/vowelcount``` 

and when you POST a word to this API, it responds back with number of vowels in
the given word. 

If you make a GET request to this API, it will respond back 
with the number of words it has dealt so far and the word with the highest 
number of vowels it has encountered.

## Using the API service
### To get the summary
```shell script
$ curl http://localhost:8000/api/vowelcount
{"message":"Welcome to Vowel Count API service!"}
```

### To post data and get vowel count
```shell script
$ curl -H "Content-Type: application/json" -X POST -d '{"word":"siddesh"}' http://localhost:8000/api/vowelcount
{"message":"The given word is siddesh!"}

# To test the error message, call api without providing data
curl -H "Content-Type: application/json" -X POST http://localhost:8000/api/vowelcount
```


## Setup
### pip packages
This project code is compliant with python 3.5 and above.
```shell script
pip install django
pip install djangorestframework
```

### Create django project - vowel_count
```shell script
django-admin startproject vowel_count
```

### Create an App - api
```shell script
cd vowel_count
python manage.py startapp api
```

### DB setup - mysql
This project uses mysql as DB. But if you want use the default SQLite as DB,
then the instructions given in this section can be skipped.
 
#### Install mysql
##### Mac
- You can download .dmg file from https://dev.mysql.com/downloads/file/?id=479114
and follow the instructions to complete the installation.
- To start the database, goto system preferences -> click on mysql -> Start

#### Login to mysql
```shell script
mysql -u root -p
```
#### Create database - vowel_count
```shell script
mysql> create database vowel_count;
mysql> show databases;
```

#### Create a DB user - vowel_counter
```shell script
mysql> create user vowel_counter@localhost identified by 'vowel_counter';

# Grant access to DB 'vowel_count' for user 'vowel_counter'
mysql> GRANT ALL PRIVILEGES ON vowel_count . * TO 'vowel_counter'@'localhost'; 
```

### Update settings.py to use mysql as DB
```shell script
vi vowel_count/vowel_count/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vowel_count',
        'USER': 'vowel_counter',
        'PASSWORD': 'vowel_counter',
    }
}
```

### Update the 'INSTALLED_APPS' config in settings.py
Update the 'INSTALLED_APPS' section in the settings.py with 'rest_framework' 
and 'api' apps.

```shell script
vi vowel_count/vowel_count/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'api'
]

``` 
###  Apply the migrations
```shell script
python manage.py migrate
```

### Start Django local server
```shell script
python manage.py runserver 

# You can access it with http://127.0.0.1:8000/
```