from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models as geo

# Create your models here.


# table governorate
class Gouvernat(models.Model):
    governorate = models.CharField(
        verbose_name=_("governorate"), max_length=30, unique=True)
    code_iso = models.CharField(verbose_name=_("code-ISO"), max_length=10)
    index_code_postal = ArrayField(models.PositiveIntegerField())
    coordinates = geo.PointField(verbose_name=_("coordinates"))

    def __str__(self):
        return f'{self.governorate}'

    class Meta:
        verbose_name = _('governorate')
        verbose_name_plural = _('governorates')


# table liste de code des postes
class CodePoste(models.Model):
    postal_code = models.CharField(verbose_name=_(
        "Postal code"), max_length=4, unique=True)

    def __str__(self):
        return f'{self.postal_code}'

    class Meta:
        verbose_name = _('Postal code')
        verbose_name_plural = _('Postal Codes')


# table city
class Ville(models.Model):
    postal_code = ArrayField(
        models.PositiveIntegerField())
    city = models.CharField(_("city"), max_length=30,
                            default='', unique=True)
    governorate = models.ForeignKey(
        Gouvernat, verbose_name=_("governorate"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.city}'

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


# table localité
class Localite(models.Model):
    locale = models.CharField(verbose_name=_(
        "locality"), max_length=50, unique=True)
    code_postal = ArrayField(
        models.PositiveIntegerField())
    city = models.ForeignKey(Ville, verbose_name=_(
        "city"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.locale}'

    class Meta:
        verbose_name = _('Locality')
        verbose_name_plural = _('Localities')


# table address
class Address(models.Model):
    street = models.CharField(verbose_name=_("street"), max_length=50)
    apartment = models.CharField(
        verbose_name=_("apartment"), max_length=50)
    floor = models.CharField(verbose_name=_("floor"), max_length=50)
    door = models.CharField(verbose_name=_("door"), max_length=50)
    comment = models.CharField(
        verbose_name=_("comment"), max_length=200)

    def __str__(self):
        return f"{self.street}"

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Address')
