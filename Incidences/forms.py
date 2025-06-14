from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import updateroad
from django.contrib.gis.geos import Point
from django import forms
from .models import updateroad

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class UpdateRoadForm(forms.ModelForm):
    class Meta:
        model = updateroad
        fields = ['location', 'desc']


class UpdateRoadForm(forms.ModelForm):
    blockage_location = forms.CharField()  # Assuming blockage_location is a CharField in the form

    class Meta:
        model = updateroad
        fields = ['location', 'desc']

    def clean_blockage_location(self):
        # Process the blockage_location field
        blockage_location_str = self.cleaned_data['blockage_location']

        # Extracting coordinates from the string
        coordinates = blockage_location_str.strip('LatLng()').split(',')
        lat, lon = map(float, coordinates)

        # Creating a Point object
        blockage_location_point = Point(lon, lat)

        return blockage_location_point
