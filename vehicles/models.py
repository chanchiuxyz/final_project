from django.db import models

# Create your models here.

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)

class Vehicles(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    brand = models.CharField(max_length=30)
    body_type = models.CharField(max_length=30)
    engine = models.CharField(max_length=10)
    passengers = models.IntegerField()
    doors = models.IntegerField()
    fuel_type = models.CharField(max_length=10)
    
    # class Meta:
    #     db_table = 'Vehicles'

class Latest_location(models.Model):
    vehicle_id = models.CharField(primary_key=True,max_length=10)
    lat = models.DecimalField(max_digits=9,decimal_places=6)
    lon = models.DecimalField(max_digits=9,decimal_places=6)
    couse = models.IntegerField()
    speed = models.IntegerField()
    altitude = models.IntegerField()
    create_time = models.DateTimeField(null=True)
