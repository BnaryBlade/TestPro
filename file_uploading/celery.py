import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_uploading.settings')

app = Celery('file_uploading')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
