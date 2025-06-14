import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import Openspace

openspace_mapping = {
    'name': 'NAME',
    'popupinfo': 'POPUPINFO',
    'shape_area': 'SHAPE_AREA',
    'geom': 'MULTIPOLYGON25D',
}

openspace_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','openspace.shp'),)

def run(verbose=True):
    lm = LayerMapping(Openspace, openspace_shp, openspace_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)