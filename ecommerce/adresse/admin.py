from import_export.admin import ImportExportModelAdmin, ImportMixin

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
    list_display = ('ville',)
    resource_class = VilleResource


@admin.register(CodePoste)
class CodePosteAdmin(ImportExportModelAdmin):
    list_display = ['code_poste']
    resource_class = CodePosteResource