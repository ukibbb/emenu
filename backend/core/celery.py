import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", "core.settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    "notify-users-about-last-created-and-updated-items": {
        "task": "accounts.tasks.notify_users_about_last_created_and_updated_items",
        "schedule": crontab(hour=10),
    }
}
