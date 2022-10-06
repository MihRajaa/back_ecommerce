from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .resources import *
from .models import *

# Register your models here.


@admin.register(Gouvernat)
class GouvernatAdmin(ImportExportModelAdmin):
    list_display = ('gouvernat', 'code_iso',
                    'index_code_postal', 'coordonnees')
    resource_class = GouvernatResource

    class Meta:
        fields = ['gouvernat', 'code_iso', 'index_code_postal', 'coordonnees']


@admin.register(Ville)
class VilleAdmin(ImportExportModelAdmin):
    list_display = ['ville', 'code_poste']
    resource_class = VilleResource

    class Meta:
        fields = ['ville', 'code_poste']


@admin.register(CodePoste)
class CodePosteAdmin(ImportExportModelAdmin):
    list_display = ['code_poste', ]
    resource_class = CodePosteResource


@admin.register(Localite)
class LocaliteAdmin(ImportExportModelAdmin):
    list_display = ['locale', 'code_postal', 'ville']
    resource_class = LocaliteResource


@admin.register(Adresse)
class AdresseAdmin(admin.ModelAdmin):
    list_display = ["appartement",
                    "etage",
                    "porte",
                    "commentaire",
                    "rue"]
