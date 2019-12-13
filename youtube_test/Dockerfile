# Start with  basic Ubuntu image
FROM ubuntu:18.04

MAINTAINER Ryan McGrane

# Install everything that you need exept libraries specific to your Django project - these come later.
# RUN pip install --upgrade pip setuptools wheel
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python3-dev python3-setuptools python3-pip libgdal-dev nginx supervisor
RUN pip3 install --upgrade pip setuptools wheel

# Make a new direcctory on your target image and set it as your working dorectory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.
COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

# add (the rest of) our code
COPY . /usr/src/app

# Set up all the configfiles
COPY django_nginx.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# Expose the image's ports. We'll bind different host ports to these later
EXPOSE 80
EXPOSE 443

# When a new container is created, we'll run supervisord to start uwsgi and nginx.
CMD ["supervisord", "-n"]