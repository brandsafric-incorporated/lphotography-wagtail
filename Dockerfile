# Use passenger as base image for a better development web application foundation
FROM phusion/passenger-full:0.9.17

MAINTAINER Christopher Smith <chris@funkyrobot.net>

# Set environment variables
ENV HOME /root

# Use the init process from baseimage-docker (the base of image of the passenger image)
CMD ["/sbin/my_init"]

# Enable nginx
RUN rm -f /etc/service/nginx/down

# Configure django site in nginx
RUN rm /etc/nginx/sites-enabled/default
ADD django-nginx.conf /etc/nginx/sites-enabled/django-nginx.conf

# Build instructions for django
# Copy application files to nginx configured location
COPY ./ /home/app

RUN apt-get update && apt-get install -y \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    python-pip \
    python-dev \
    build-essential

RUN /usr/bin/pip install -r /home/app/requirements.txt

RUN /usr/bin/python /home/app/manage.py collectstatic --noinput

EXPOSE 80
