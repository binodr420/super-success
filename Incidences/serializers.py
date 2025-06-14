from rest_framework import serializers
from Incidences.models import Building,CAGB,Finance,Openspace,Road,School,Health, Ward,Waterway

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('name', 'type', 'geom')

class CAGBSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAGB
        fields = ('name', 'geom')

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = ('name', 'geom')

class OpenspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Openspace
        fields = ('id', 'name', 'popupinfo', 'shape_area', 'geom')

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = ('id', 'name', 'type', 'shape_len', 'geom')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'geom')

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ('name', 'geom')

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'

class WaterwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Waterway
        fields = ('id', 'shape_leng', 'name', 'type', 'width', 'geom')




