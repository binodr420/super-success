import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import Health

health_mapping = {
    'name': 'Name',
    'geom': 'MULTIPOINT25D',
}

health_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','health.shp'),)

def run(verbose=True):
    lm = LayerMapping(Health, health_shp, health_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)