import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import Waterway

waterways_mapping = {
    'shape_leng': 'SHAPE_LENG',
    'name': 'NAME',
    'type': 'TYPE',
    'width': 'WIDTH',
    'geom': 'MULTILINESTRING',
}

waterways_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','waterways.shp'),)

def run(verbose=True):
    lm = LayerMapping(Waterway, waterways_shp, waterways_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)