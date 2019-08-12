#!/bin/bash
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py process_tasks
echo 'It worked!!'