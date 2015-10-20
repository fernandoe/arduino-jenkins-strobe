### Run the Application ###
```
docker run --rm \
           --device=/dev/ttyACM0 \
           -v /opt/arduino:/db \
           -e "http_proxy=http://16.85.175.150:8088" \
           -e "https_proxy=http://16.85.175.150:8088" \
           -p 8000:8000 \
           -i \
           -t fernandoe/arduino-jenkins-strobe
```


### Migrations ###
```
python manage.py makemigrations jenkins
python manage.py migrate
```

### Docker for Development ###
```
docker build --no-cache=false -t arduino .
docker run --rm --device=/dev/ttyACM0 -v $(pwd)/arduino:/app -v /opt/arduino:/db -v ./sandbox/docker/home:/root -p 8000:8000 -p 1338:22 -i -t arduino /bin/bash
# docker run -t -i --device=/dev/ttyUSB0 ubuntu bash
```


### Celery ###
```
celery -A arduino  worker -B -l info -S djcelery.schedulers.DatabaseScheduler
```


### Dockerfile Examples ###
```
RUN python manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell
```


#### Add in the Dockerfile to use with PyCharm ####
```
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
EXPOSE 22
```