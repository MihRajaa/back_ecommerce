import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re
from django.contrib.gis.geos import Point


from .models import *


@receiver(pre_save, sender=Ville)
def recherche_gouvernat(sender, instance, **kwargs):
    index = []
    for c in instance.code_poste:
        index.append(int(str(c)[:2]))

    gouv = Gouvernat.objects.get(index_code_postal__contains=[index[0]])

    if not gouv:
        logging.warning("Validation")
    else:
        logging.warning(gouv)
        instance.gouvernat = gouv


@receiver(pre_save, sender=Localite)
def recherche_ville(sender, instance, **kwargs):
    ville = Ville.objects.get(code_poste__contains=instance.code_postal)

    if not ville:
        logging.warning("n'existe pas")
    else:
        logging.warning(ville)
        instance.ville = ville


# @receiver(pre_save, sender=Gouvernat)
# def calcul_coordonnees(sender, instance, **kwargs):
#     # methode 1
#     cord = []
#     logging.warning(instance.coordonnees)
#     for s in re.findall(r'\b\d+\b', instance.coordonnees):
#         cord.append(int(s))

#     coordonnees = Point((cord[0]+cord[1]/60+cord[2]/3600),
#                         (cord[3]+cord[4]/60+cord[5]/3600))

#     instance.coordonnees = coordonnees

    # Methode 2
    # from geopy.geocoders import Nominatim
    # geolocator = Nominatim(user_agent="geoapiExercises")
    # address = geolocator.geocode(instance.coordonnees)
    # print(address.latitude, address.longitude)
    # instance.coordonnees = address
