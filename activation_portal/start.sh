#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata fixtures/users.json 
gunicorn -b 0.0.0.0:8000 --workers 3 --log-level=info app.wsgi 
