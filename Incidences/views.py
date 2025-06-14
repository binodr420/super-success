from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.http import JsonResponse, HttpResponseBadRequest,response
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
import requests
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
import polyline
import osmnx as ox
from networkx.readwrite import json_graph
from django.contrib.gis.geos import Point
from django.views.generic import TemplateView
from Incidences.models import Building,CAGB,Finance,Openspace,Road,School,Health, Ward,Waterway,proad,Contact,updateroad #landslide,SusceptibilityMap
from django.core.serializers import serialize
from django.contrib.gis.db.models.functions import Distance
ox.config(log_console=True, use_cache=True)
from django.contrib import messages
from .forms import UpdateRoadForm
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'map.html'

class about(TemplateView):
	template_name = 'about.html'

class contact(TemplateView):
	template_name = 'contact.html'
	
class UpdateRoad(CreateView):
       model = updateroad
       form_class = UpdateRoadForm
       template_name = 'update_road.html'
	   
class UpdateRoad(CreateView):
    model = updateroad
    form_class = UpdateRoadForm
    template_name = 'update_road.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return JsonResponse({'status': 'success'})


def savemessage(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('Email id')
        phone = request.POST.get('Phone Number')
        desc = request.POST.get('How can we help you??')
        msg = Contact(name=firstname, lname=lastname, email=email, phone=phone, desc=desc)
        msg.save()
        messages.success(request,'Thank you for contacting us😊😊' )
	  
    return render(request, "contact.html")
		

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Retrieve 'username' from POST data
        password = request.POST.get('password')  # Retrieve 'password' from POST data

        # Authenticate the user using the retrieved username and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

    context = {}
    return render(request, 'login.html', context)

	
def registration(request):
	form = CreateUserForm()
	
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account was created for' + user)
			
			return redirect('login')
		

	context = {'form':form}
	return render(request,'registration.html',context)
	
class community_building(TemplateView):
	template_name ='community_building.html'
	
class financial_institution(TemplateView):
	template_name ='financial_institution.html'
	
class health_facility(TemplateView):
	template_name ='health_facility.html'
	
class houses(TemplateView):
	template_name ='houses.html'
	
class openspace(TemplateView):
	template_name ='openspace.html'
	
class road(TemplateView):
	template_name ='road.html'
	
class schools(TemplateView):
	template_name ='schools.html'
	
class waterways(TemplateView):
	template_name ='waterways.html'
	

def building_datasets(request):
	building = serialize('geojson', Building.objects.all())
	return HttpResponse(building,content_type='json')

def cagb_datasets(request):
	cagb = serialize('geojson', CAGB.objects.all())
	return HttpResponse(cagb,content_type='json')

def finance_datasets(request):
	finance = serialize('geojson', Finance.objects.all())
	return HttpResponse(finance,content_type='json')

def openspace_datasets(request):
	openspace = serialize('geojson', Openspace.objects.all())
	return HttpResponse(openspace,content_type='json')

def road_datasets(request):
	road = serialize('geojson', Road.objects.all())
	return HttpResponse(road,content_type='json')

def proad_datasets(request):
	poroad = serialize('geojson', proad.objects.all())
	return HttpResponse(poroad,content_type='json')

#def susceptibilityMap_datasets(request):
#def landslide_landslidedatasets(request):

def school_datasets(request):
	school = serialize('geojson', School.objects.all())
	return HttpResponse(school,content_type='json')

def health_datasets(request):
	health = serialize('geojson', Health.objects.all())
	return HttpResponse(health,content_type='json')

def ward_datasets(request):
	ward = serialize('geojson', Ward.objects.all())
	return HttpResponse(ward,content_type='json')

def waterway_datasets(request):
	waterway = serialize('geojson', Waterway.objects.all())
	return HttpResponse(waterway,content_type='json')
#get route
def get_route(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat):
    loc = "{},{};{},{}".format(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat)
    url = "http://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc) 
    if r.status_code!= 200:
        return {}
    res = r.json()   
    routes = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][1]['location'][1], res['waypoints'][1]['location'][0]]
    distance = res['routes'][0]['distance']
    
    out = {'route':routes,
           'start_point':start_point,
           'end_point':end_point,
           'distance':distance
          }

    return out


def search_facility(request):
    # Get the user's position from the request parameters
    latitude = float(request.GET.get('latitude', '0'))
    longitude = float(request.GET.get('longitude', '0'))
    user_position = Point(longitude, latitude, srid=4326)

    # Find the nearest critical facility based on the user's search
    search_type = request.GET.get('searchType')
    print(search_type)
    facilities=None
    if search_type == 'hospital':
        facilities = Health.objects.annotate(distance=Distance('geom', user_position)).order_by('distance')
    elif search_type == 'openspace':
        facilities = Openspace.objects.annotate(distance=Distance('geom', user_position)).order_by('distance')
    elif search_type == 'school':
        facilities = School.objects.annotate(distance=Distance('geom', user_position)).order_by('distance')
    elif search_type == 'CAGB':
        facilities = CAGB.objects.annotate(distance=Distance('geom', user_position)).order_by('distance')
    elif search_type == 'finance':
        facilities = Finance.objects.annotate(distance=Distance('geom', user_position)).order_by('distance')
    nearest_facility = facilities.first()
    print(nearest_facility.name) 
    # Define two points
    
    point1 = (user_position.x, user_position.y)
    point2 = (nearest_facility.geom.coords[0])
    print(point2[0])
    route=get_route(user_position.x,user_position.y,point2[0],point2[1])
    print(route.values())
  

   

    # Prepare the data to be sent as JSON response
    response_data = {
        'user_position': [user_position.x, user_position.y],
        'nearest_facility': {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [point2[0],point2[1]],
            },
            'properties': {
                'name': nearest_facility.name, # Replace 'name' with the appropriate field name in your model
            },
        },
        'shortest_path': {
            'type': 'Feature',
            'geometry': {
                'type': 'LineString',
                'coordinates': route['route'],
            },
        },
    }

    return JsonResponse(response_data)
    
