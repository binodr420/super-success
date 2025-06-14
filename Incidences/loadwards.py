import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import Ward

wards_mapping = {
    'dcode': 'DCODE',
    'district': 'DISTRICT',
    'gapa_napa': 'GAPA_NAPA',
    'type_gn': 'TYPE_GN',
    'new_ward_n': 'NEW_WARD_N',
    'area_sqkm': 'AREA_SQKM',
    'shape_area': 'SHAPE_AREA',
    'geom': 'MULTIPOLYGON',
}

wards_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','wards.shp'),)

def run(verbose=True):
    lm = LayerMapping(Ward, wards_shp, wards_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)