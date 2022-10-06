from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField
# from django.contrib.gis.db import models

# Create your models here.


# table gouvernat
class Gouvernat(models.Model):
    gouvernat = models.CharField(max_length=30)
    code_iso = models.CharField(max_length=10)
    index_code_postal = ArrayField(models.PositiveIntegerField())
    coordonnees = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.gouvernat}'


# table liste de code des postes
class CodePoste(models.Model):
    code_poste = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.code_poste}'


# table ville
class Ville(models.Model):
    code_poste = ArrayField(
        models.PositiveIntegerField())
    ville = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'{self.ville}'


# table localité
class Localite(models.Model):
    locale = models.CharField(max_length=50)
    code_postal = ArrayField(
        models.PositiveIntegerField())
    ville = models.ForeignKey('Ville', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.locale}'


# table adresse
class Adresse(models.Model):
    appartement = models.CharField(_(""), max_length=50)
    etage = models.CharField(_(""), max_length=50)
    porte = models.CharField(_(""), max_length=50)
    commentaire = models.CharField(_(""), max_length=200)
    rue = models.CharField(_(""), max_length=50)

    def __str__(self):
        return f"{self.rue}"
