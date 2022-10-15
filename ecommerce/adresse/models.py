from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models as geo

# Create your models here.


# table gouvernat
class Gouvernat(models.Model):
    gouvernat = models.CharField(verbose_name=_(
        "gouvernat"), max_length=30, unique=True)
    code_iso = models.CharField(verbose_name=_("code-ISO"), max_length=10)
    index_code_postal = ArrayField(models.PositiveIntegerField())
    coordonnees = geo.PointField()

    def __str__(self):
        return f'{self.gouvernat}'

# table liste de code des postes


class CodePoste(models.Model):
    code_poste = models.CharField(verbose_name=_(
        "code poste"), max_length=4, unique=True)

    def __str__(self):
        return f'{self.code_poste}'


# table ville
class Ville(models.Model):
    code_poste = ArrayField(
        models.PositiveIntegerField())
    ville = models.CharField(_("ville"), max_length=30,
                             default='', unique=True)
    gouvernat = models.ForeignKey(
        Gouvernat, verbose_name=_("gouvernat"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.ville}'


# table localité
class Localite(models.Model):
    locale = models.CharField(verbose_name=_(
        "locale"), max_length=50, unique=True)
    code_postal = ArrayField(
        models.PositiveIntegerField())
    ville = models.ForeignKey(Ville, verbose_name=_(
        "ville"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.locale}'


# table adresse
class Adresse(models.Model):
    rue = models.CharField(verbose_name=_("rue"), max_length=50)
    appartement = models.CharField(
        verbose_name=_("appartement"), max_length=50)
    etage = models.CharField(verbose_name=_("étage"), max_length=50)
    porte = models.CharField(verbose_name=_("porte"), max_length=50)
    commentaire = models.CharField(
        verbose_name=_("commentaire"), max_length=200)

    def __str__(self):
        return f"{self.rue}"
