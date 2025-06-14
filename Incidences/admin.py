from django.contrib import admin
from django.contrib.gis import admin
from .models import Building,CAGB,Finance,Health,Openspace,Road,School,Ward,Waterway,proad,Contact,updateroad
# yasle kam gari raa ko xaina from leaflet.admin import LeafletGeoAdmin
#class 
# Register your models here.
#admin.site.register(Building,admin.ModelAdmin)
#admin.site.register(CAGB,admin.ModelAdmin)
#admin.site.register(Finance,admin.ModelAdmin)
#admin.site.register(Health,admin.ModelAdmin)
#admin.site.register(Openspace,admin.ModelAdmin)
#admin.site.register(School,admin.ModelAdmin)
#admin.site.register(Ward,admin.ModelAdmin)
#admin.site.register(Waterway,admin.ModelAdmin)
class BuildingAdmin(admin.ModelAdmin):
    list_display=('name','type','geom')
admin.site.register(Building,BuildingAdmin)

class CAGBAdmin(admin.ModelAdmin):
    list_display=('name','geom')
admin.site.register(CAGB,CAGBAdmin)

class FinanceAdmin(admin.ModelAdmin):
    list_display=('name','geom')
admin.site.register(Finance,FinanceAdmin)

class HealthAdmin(admin.ModelAdmin):
    list_display=('name','geom')
admin.site.register(Health,HealthAdmin)

class OpenspaceAdmin(admin.ModelAdmin):
    list_display=('name','popupinfo','shape_area','geom')
admin.site.register(Openspace,OpenspaceAdmin)

class SchoolAdmin(admin.ModelAdmin):
    list_display=('name','geom')
admin.site.register(School,SchoolAdmin)

class WardAdmin(admin.ModelAdmin):
    list_display=('dcode','district','gapa_napa','type_gn','new_ward_n','area_sqkm','shape_area','geom')
admin.site.register(Ward,WardAdmin)

class WaterwayAdmin(admin.ModelAdmin):
    list_display=('shape_leng','name','type','width','geom')
admin.site.register(Waterway,WaterwayAdmin)

class RoadAdmin(admin.ModelAdmin):
    list_display=('name','type','shape_len','geom')
admin.site.register(Road,RoadAdmin)

class ProadAdmin(admin.ModelAdmin):
    list_display=('name','type','shape_len','geom')
admin.site.register(proad,ProadAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','desc')
admin.site.register(Contact,ContactAdmin)

class updateroadAdmin(admin.ModelAdmin):
    list_display=('location','desc')
admin.site.register(updateroad,updateroadAdmin)