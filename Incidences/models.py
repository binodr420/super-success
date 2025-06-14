from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=254,null=True)
    type = models.CharField(max_length=254,null=True)
    geom = models.MultiPolygonField(srid=4326)
    class meta:
        db_table ='Building'
    def __str__(self):
     return self.name


class CAGB(models.Model):
    name = models.CharField(max_length=48)
    geom = models.MultiPolygonField(srid=4326)
    class meta:
        db_table ='cagb'
    def __str__(self):
     return self.name


class Finance(models.Model):
    name = models.CharField(max_length=48)
    geom = models.MultiPointField(srid=4326)
    class meta:
        db_table='finance'
    def __str__(self):
     return self.name

class Health(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)
    class meta:
        db_table='Health'
    def __str__(self):
     return self.name

class Openspace(models.Model):
    name = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    class meta:
        db_table='Openspace'
    def __str__(self):
     return self.name


class Road(models.Model):
    name = models.CharField(max_length=48,null=True)
    type = models.CharField(max_length=16)
    shape_len = models.FloatField(null=True)
    geom = models.MultiLineStringField(srid=4326)
    class meta:
        db_table='Roads'
    def __str__(self):
     return self.name
    
class proad(models.Model):
    name = models.CharField(max_length=48,null=True)
    type = models.CharField(max_length=16)
    shape_len = models.FloatField(null=True)
    geom = models.MultiLineStringField(srid=4326)
    class meta:
        db_table='PRoads'
    def __str__(self):
     return self.name



class School(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)
    class meta:
        db_table='School'
    def __str__(self):
     return self.name


class Ward(models.Model):
    dcode = models.BigIntegerField()
    district = models.CharField(max_length=50)
    gapa_napa = models.CharField(max_length=50)
    type_gn = models.CharField(max_length=50)
    new_ward_n = models.BigIntegerField()
    area_sqkm = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    class meta:
        db_table='Wards'
    def __str__(self):
     return self.name


class Waterway(models.Model):
    shape_leng = models.FloatField()
    name = models.CharField(max_length=48 ,null=True)
    type = models.CharField(max_length=16)
    width = models.IntegerField()
    geom = models.MultiLineStringField(srid=4326)
    class meta:
        db_table='Waterways'
    def __str__(self):
     return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    lname= models.CharField(max_length=100, default='')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class updateroad(models.Model):
    location = models.MultiPointField(srid=4326)
    desc = models.TextField()

    def __str__(self):
        return f"Updateroad - {self.location}"
    