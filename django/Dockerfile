FROM python:2.7-onbuild
RUN python manage.py collectstatic --noinput
CMD uwsgi --socket :8001 --module lphotography.wsgi
