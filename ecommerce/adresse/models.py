from enum import unique
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models as geo
from location_field.models.spatial import LocationField
# from osgeo import gdal

# Create your models here.


# table gouvernat
class Gouvernat(models.Model):
    gouvernat = models.CharField(max_length=30, unique=True)
    code_iso = models.CharField(max_length=10)
    index_code_postal = ArrayField(models.PositiveIntegerField())
    coordonnees = geo.PointField()

    # @coordonnees.setter
    # def coordonnees(self, value):
    #     print(value)
    #     self.coordonnees = value

    def __str__(self):
        return f'{self.gouvernat}'

    # def save(self, *args, **kwargs):
    #     print(self.coordonnees)


# table liste de code des postes
class CodePoste(models.Model):
    code_poste = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f'{self.code_poste}'


# table ville
class Ville(models.Model):
    code_poste = ArrayField(
        models.PositiveIntegerField())
    ville = models.CharField(max_length=30, default='', unique=True)
    gouvernat = models.ForeignKey(
        Gouvernat, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.ville}'


# table localité
class Localite(models.Model):
    locale = models.CharField(max_length=50, unique=True)
    code_postal = ArrayField(
        models.PositiveIntegerField())
    ville = models.ForeignKey('Ville', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.locale}'


# table adresse
class Adresse(models.Model):
    rue = models.CharField(_(""), max_length=50)
    appartement = models.CharField(_(""), max_length=50)
    etage = models.CharField(_(""), max_length=50)
    porte = models.CharField(_(""), max_length=50)
    commentaire = models.CharField(_(""), max_length=200)

    def __str__(self):
        return f"{self.rue}"
