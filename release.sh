#!/bin/bash
python3 manage.py migrate
python3 manage.py collectstatic
echo 'It worked!!'