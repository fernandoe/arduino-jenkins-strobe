### Migrations ###
```
#!shell
python manage.py makemigrations jenkins
python manage.py migrate
```

### Docker ###
```
#!shell
docker build --no-cache=true -t arduino .
docker run --rm -v $(pwd)/arduino:/app -p 8000:8000 -p 22:1338 -i -t arduino /bin/bash
```


### Celery ###
```
#!shell
celery -A arduino  worker -B -l info -S djcelery.schedulers.DatabaseScheduler
```
