import os
from django.contrib.gis.utils import LayerMapping
from Incidences.models import CAGB

cagb_mapping = {
    'name': 'NAME',
    'geom': 'MULTIPOLYGON',
}

cagb_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','cagbuilding.shp'),)

def run(verbose=True):
    lm = LayerMapping(CAGB, cagb_shp, cagb_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)