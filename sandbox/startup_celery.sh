#!/bin/bash
cd /app

while [ -z "`netstat -tln | grep 8000`" ]; do
  echo 'Waiting for Django to start ...'
  sleep 3
done
echo 'Django started.'

echo 'Starting celery...'
celery -A arduino  worker -B -l info -S djcelery.schedulers.DatabaseScheduler
