import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re
from django.contrib.gis.geos import Point


from .models import *


@receiver(pre_save, sender=Ville)
def recherche_gouvernat(sender, instance, **kwargs):
    index = []
    for c in instance.postal_code:
        index.append(int(str(c)[:2]))

    gouv = Gouvernat.objects.get(index_code_postal__contains=[index[0]])

    if not gouv:
        logging.warning("Validation")
    else:
        logging.warning(gouv)
        instance.governorate = gouv


@receiver(pre_save, sender=Localite)
def recherche_ville(sender, instance, **kwargs):
    city = Ville.objects.get(code_poste__contains=instance.code_postal)

    if not city:
        logging.warning("n'existe pas")
    else:
        logging.warning(city)
        instance.city = city
