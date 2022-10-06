from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import *


@receiver(pre_save, sender=Ville)
def recherche_gouvernat(sender, instance, **kwargs):
    index = []
    for c in instance.code_poste:
        index.append(int(str(c)[:2]))

    gouv = Gouvernat.objects.get(index_code_postal=index[0])

    if not gouv:
        print("verifier votre code poste")
    else:
        print("valide code poste")
