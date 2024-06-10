from django.shortcuts import render
from django.http import HttpResponse
#REST framework
from rest_framework import permissions,viewsets
from .models import Vehicles,Latest_location
from vehicles.serializers import VehicleSerializer,Lastest_locationSerializer

# Create your views here.
def index(request) :
    return HttpResponse('vehicels pages')


class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

class Latest_locationViewSet(viewsets.ModelViewSet):
    queryset = Latest_location.objects.all().order_by('create_time')
    serializer_class = Lastest_locationSerializer
    permission_classes = [permissions.IsAuthenticated]

