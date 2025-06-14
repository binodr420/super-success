import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import Building

building_mapping = {
    'name': 'NAME',
    'type': 'TYPE',
    'geom': 'MULTIPOLYGON',
}

building_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','buildings.shp'),)

def run(verbose=True):
    lm = LayerMapping(Building, building_shp, building_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)