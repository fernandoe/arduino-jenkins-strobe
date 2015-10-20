#!/bin/bash
cd /app

echo 'Running migrations...'
python manage.py migrate

echo 'Starting server...'
gunicorn -c /opt/arduino/gunicorn_config.py arduino.wsgi
