# -*- coding:utf-8 -*-
from __future__ import absolute_import

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ansible_sample_app.settings")

from celery import Celery

from django.conf import settings

app = Celery('ansible_sample_app', broker=settings.BROKER_URL)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
