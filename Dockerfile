FROM python:3.10.5
LABEL version="1.0.0"



WORKDIR ./


ADD ./ ./
COPY ./requirements.txt /etc

RUN apt update
RUN apt install nginx -y
RUN /etc/init.d/nginx start
RUN python -m pip install --upgrade pip
RUN pip install -r /etc/requirements.txt

ONBUILD RUN apt install apache2
ONBUILD CMD service apache2 start
ONBUILD RUN apt install php-gettext libapache2-mod-php
ONBUILD RUN apt install mysql-server
ONBUILD CMD  service mysql restart
ONBUILD RUN apt install phpmyadmin
ONBUILD CMD service apache2 restart

EXPOSE 80/tcp
EXPOSE 80/udp
EXPOSE 3306/tcp
EXPOSE 3306/udp
EXPOSE 443/tcp
EXPOSE 443/udp

COPY ./ ./

CMD ["python", "Main.py"]





