FROM fernandoe/python:0.0.1
MAINTAINER Fernando Espíndola <fer.esp@gmail.com>

RUN mkdir -p /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY ./arduino /app

RUN python manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

EXPOSE 8000

# CMD [ "gunicorn", "-c", "gunicorn_config.py", "wsgi:application" ]

# To use in PyCharm
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
EXPOSE 22
