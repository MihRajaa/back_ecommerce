from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .resources import *
from .models import *

# Register your models here.


@admin.register(Gouvernat)
class GouvernatAdmin(ImportExportModelAdmin):
    list_display = ('governorate', 'code_iso',
                    'index_code_postal', 'coordinates')
    resource_class = GouvernatResource

    class Meta:
        fields = ['governorate', 'code_iso',
                  'index_code_postal', 'coordinates']


@admin.register(Ville)
class VilleAdmin(ImportExportModelAdmin):
    list_display = ['city', 'postal_code']
    resource_class = VilleResource

    class Meta:
        fields = ['city', 'postal_code']


@admin.register(CodePoste)
class CodePosteAdmin(ImportExportModelAdmin):
    list_display = ['postal_code', ]
    resource_class = CodePosteResource


@admin.register(Localite)
class LocaliteAdmin(ImportExportModelAdmin):
    list_display = ['locale', 'code_postal', 'city']
    resource_class = LocaliteResource


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["apartment",
                    "floor",
                    "door",
                    "comment",
                    "street"]
