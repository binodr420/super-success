import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import Finance

finance_mapping = {
    'name': 'NAME',
    'geom': 'MULTIPOINT25D',
}

finance_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','finance.shp'),)

def run(verbose=True):
    lm = LayerMapping(Finance, finance_shp, finance_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)