from rest_framework import serializers
from .models import Vehicles,Latest_location


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['id','brand','body_type','engine','passengers','doors','fuel_type']

class Lastest_locationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Latest_location
        fields = ['vehicle_id','lat','lon','couse','speed','altitude','create_time']


