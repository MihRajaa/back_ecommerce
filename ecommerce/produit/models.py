from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.


class Categorie(models.Model):
    name = models.CharField(verbose_name=_("category name"), max_length=50)
    slug = models.SlugField(_(""))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Produit(models.Model):
    category = models.ForeignKey(
        "Categorie", verbose_name=_("Category"), related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(_(""))
    description = models.CharField(
        verbose_name=_("Description"), max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=3)
    image = models.ImageField(
        upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to='uploads/',  blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-date_added",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.categorie.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000/' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000/' + self.thumbnail.url
        else:

            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000/' + self.thumbnail.url

            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
