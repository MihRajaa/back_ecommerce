from django.contrib import admin

from .models import Produit, Categorie
# Register your models here.


@admin.register(Produit)
class ProduitRegister(admin.ModelAdmin):
    pass


@admin.register(Categorie)
class CategorieRegister(admin.ModelAdmin):
    pass
