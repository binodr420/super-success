import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import proad

proads_mapping = {
    'name': 'NAME',
    'type': 'TYPE',
    'shape_len': 'SHAPE_LEN',
    'geom': 'MULTILINESTRING',
}

proads_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','Pokhara_Roads_5.shp'),)

def run(verbose=True):
    lm = LayerMapping(proad, proads_shp, proads_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)