#!/bin/bash

# This file controls the automatic migrations 
# When deployed to heroku

python3 manage.py makemigrations
python3 manage.py migrate
echo 'It worked!!'