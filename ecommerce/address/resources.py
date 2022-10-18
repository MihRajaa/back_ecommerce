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
        attribute='strcoordonnees', column_name='coordinates')
    index_code_postal = fields.Field(
        column_name='index_code_postal',
        attribute='index_code_postal',
        widget=widgets.SimpleArrayWidget(separator=';')
    )

    import_id_fields = ("governorate",)
    fields = ('governorate', 'code_iso',
              'index_code_postal', 'strcoordonnees')
    clean_model_instances = True
    export_order = ['governorate', 'code_iso',
                    'index_code_postal', 'coordinates']

    class Meta:
        model = Gouvernat

    def before_import_row(self, row, row_number=None, **kwargs):
        '''
        recu string valeur(kartography type maps address) puis extract les valeur point et faire le calcul pour get donnees au point type field
        '''

        logging.warning(row['coordinates'])
        cord = []
        coordinates = Point(0, 0)
        for s in re.findall(r'\b\d+\b', row['coordinates']):
            cord.append(int(s))
        print(len(cord))
        try:
            coordinates = Point((cord[0]+cord[1]/60+cord[2]/3600),
                                (cord[3]+cord[4]/60+cord[5]/3600))
        except:
            pass
        logging.warning(coordinates)
        row['coordinates'] = coordinates


# resource de Ville
class VilleResource(resources.ModelResource):
    code_postal = fields.Field(
        column_name='code_postal',
        attribute='code_postal',
        widget=ForeignKeyWidget(CodePoste, 'code_postal'))

    class Meta:
        model = Ville
        import_id_fields = ('code_postal', 'city',)
        fields = ('code_postal', 'city')


# resource de code de poste
class CodePosteResource(resources.ModelResource):

    class Meta:
        model = CodePoste


# resource de localite
class LocaliteResource(resources.ModelResource):
    city = fields.Field(
        column_name='city',
        attribute='city',
        widget=ForeignKeyWidget(Ville, 'city'))

    class Meta:
        model = Localite
