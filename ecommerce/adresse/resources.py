from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget

from .models import *


# resources des tables pour import export
# resource de Gouvernat
class GouvernatResource(resources.ModelResource):

    class Meta:
        index_code_postal = fields.Field(
            column_name='index_code_postal',
            attribute='index_code_postal',
            widget=widgets.SimpleArrayWidget(separator=';')
        )
        model = Gouvernat
        import_id_fields = ("gouvernat",)
        fields = ('gouvernat', 'code_iso', 'index_code_postal', 'coordonnees')


# resource de Ville
class VilleResource(resources.ModelResource):
    code_postal = fields.Field(
        column_name='code_postal',
        attribute='code_postal',
        widget=ForeignKeyWidget(CodePoste, 'code_postal'))

    class Meta:
        model = Ville
        import_id_fields = ('code_postal', 'ville',)
        fields = ('code_postal', 'ville')


# resource de code de poste
class CodePosteResource(resources.ModelResource):

    class Meta:
        model = CodePoste