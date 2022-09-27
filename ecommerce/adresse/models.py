from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField

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
    code_postal = models.ForeignKey(
        CodePoste, on_delete=models.CASCADE)
    ville = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'{self.ville, self.code_postal}'
