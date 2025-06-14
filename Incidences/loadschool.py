import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import School

school_mapping = {
    'name': 'Name',
    'geom': 'MULTIPOINT25D',
}

school_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','school.shp'),)

def run(verbose=True):
    lm = LayerMapping(School, school_shp, school_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)