#!/bin/bash
python3 manage.py migrate
python3 manage.py collectstatic --noinput

python3 worker.py # From redis

echo 'It worked!!'