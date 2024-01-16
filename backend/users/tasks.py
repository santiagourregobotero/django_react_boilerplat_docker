from django.core import management

from new_site_dbp import celery_app


@celery_app.task
def clearsessions():
    management.call_command("clearsessions")
