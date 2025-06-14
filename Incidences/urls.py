from django.urls import re_path
from Incidences.views import HomePageView,building_datasets,cagb_datasets,finance_datasets,openspace_datasets,road_datasets,school_datasets
from Incidences.views import health_datasets,ward_datasets,waterway_datasets,search_facility,about,contact,UpdateRoad,proad_datasets,user_login
from Incidences.views import registration,community_building,financial_institution,health_facility,houses,openspace,road,schools,waterways,savemessage
urlpatterns = [
    re_path(r'^$', HomePageView.as_view(), name = 'home'),
	re_path(r'^building_datasets/$', building_datasets, name = 'building'),
    re_path(r'^cagb_datasets/$', cagb_datasets, name = 'cagb'),
    re_path(r'^finance_datasets/$', finance_datasets, name = 'finance'),
    re_path(r'^openspace_datasets/$', openspace_datasets, name = 'openspace'),
    re_path(r'^road_datasets/$', road_datasets, name = 'road'),
    re_path(r'^proad_datasets/$', proad_datasets, name = 'proad'),
    re_path(r'^school_datasets/$', school_datasets, name = 'school'),
    re_path(r'^health_datasets/$', health_datasets, name = 'health'),
    re_path(r'^ward_datasets/$', ward_datasets, name = 'ward'),
    re_path(r'^waterway_datasets/$', waterway_datasets, name = 'waterway'),
    re_path(r'^about/$', about.as_view(), name = 'about'),
    re_path(r'^contact/$', contact.as_view(), name = 'contact'),
    re_path(r'^UpdateRoad/$', UpdateRoad.as_view(), name = 'UpdateRoad'),
    re_path(r'^savemessage/$', savemessage, name = 'savemessage'),

    re_path(r'^login/$', user_login, name = 'login'),
    re_path(r'^registration/$', registration, name = 'registration'),
    re_path(r'^community_building/$', community_building.as_view(), name = 'community building'),
    re_path(r'^financial_institution/$', financial_institution.as_view(), name = 'financial institution'),
    re_path(r'^health_facility/$', health_facility.as_view(), name = 'health facility'),
    re_path(r'^houses/$', houses.as_view(), name = 'houses'),
    re_path(r'^openspace/$', openspace.as_view(), name = 'open space'),
    re_path(r'^road/$', road.as_view(), name = 'Road'),
    re_path(r'^schools/$', schools.as_view(), name = 'Schools'),
    re_path(r'^waterways/$', waterways.as_view(), name = 'Waterways'),
    re_path(r'^search_facility/$', search_facility, name = 'search'),
	]

