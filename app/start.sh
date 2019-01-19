#!/usr/bin/env bash
python manage.py collectstatic --noinput
gunicorn --workers=1 --bind=0.0.0.0:8000 webapp.wsgi:application