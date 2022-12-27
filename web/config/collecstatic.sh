#!/bin/sh
cd /app/
/opt/venv/bin/python manage.py collectstatic --noinput
