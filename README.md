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

## Setup
### pip packages
This project code is compliant with python 3.5 and above.
```shell script
pip install django
```