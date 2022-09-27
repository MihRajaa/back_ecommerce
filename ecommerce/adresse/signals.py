from django.dispatch import receiver
from import_export.signals import post_import, post_export

from .models import *


@receiver(post_import, sender=Gouvernat, dispatch_uid='gouvernat')
def _post_import(model, **kwargs):
    # model is the actual model instance which after import
    pass


@receiver(post_export, dispatch_uid='gouvernat')
def _post_export(model, **kwargs):
    # model is the actual model instance which after export
    pass
