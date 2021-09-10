release: python manage.py migrate
web: gunicorn aboutme.wsgi