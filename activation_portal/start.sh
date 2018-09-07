#!/bin/bash
dockerize -wait tcp://postgresql:5432
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py create-admin
gunicorn -b 0.0.0.0:8000 --workers 3 --log-level=info app.wsgi 
