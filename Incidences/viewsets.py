from rest_framework import viewsets
from Incidences.models import Building,CAGB,Finance,Openspace,Road,School,Health, Ward,Waterway
from Incidences.serializers import BuildingSerializer,CAGBSerializer,FinanceSerializer,OpenspaceSerializer,RoadSerializer,SchoolSerializer,HealthSerializer,WardSerializer,WaterwaySerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class CAGBViewSet(viewsets.ModelViewSet):
    queryset = CAGB.objects.all()
    serializer_class = CAGBSerializer

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer

class OpenspaceViewSet(viewsets.ModelViewSet):
    queryset = Openspace.objects.all()
    serializer_class = OpenspaceSerializer

class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class HealthViewSet(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class WaterwayViewSet(viewsets.ModelViewSet):
    queryset = Waterway.objects.all()
    serializer_class = WaterwaySerializer