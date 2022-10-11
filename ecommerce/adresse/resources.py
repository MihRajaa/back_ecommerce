import logging
from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget
import re
from django.contrib.gis.geos import Point

from .models import *


# resources des tables pour import export
# resource de Gouvernat
class GouvernatResource(resources.ModelResource):
    strcoordonnees = fields.Field(
        attribute='strcoordonnees', column_name='coordonnees')
    index_code_postal = fields.Field(
        column_name='index_code_postal',
        attribute='index_code_postal',
        widget=widgets.SimpleArrayWidget(separator=';')
    )

    import_id_fields = ("gouvernat",)
    fields = ('gouvernat', 'code_iso',
              'index_code_postal', 'strcoordonnees')
    clean_model_instances = True
    export_order = ['gouvernat', 'code_iso',
                    'index_code_postal', 'coordonnees']

    class Meta:
        model = Gouvernat

    def before_import_row(self, row, row_number=None, **kwargs):
        logging.warning(row['coordonnees'])
        cord = []
        coordonnees = Point(0, 0)
        for s in re.findall(r'\b\d+\b', row['coordonnees']):
            cord.append(int(s))
        print(len(cord))
        try:
            coordonnees = Point((cord[0]+cord[1]/60+cord[2]/3600),
                                (cord[3]+cord[4]/60+cord[5]/3600))
        except:
            pass
        logging.warning(coordonnees)
        row['coordonnees'] = coordonnees


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


# resource de localite
class LocaliteResource(resources.ModelResource):
    ville = fields.Field(
        column_name='ville',
        attribute='ville',
        widget=ForeignKeyWidget(Ville, 'ville'))

    class Meta:
        model = Localite
