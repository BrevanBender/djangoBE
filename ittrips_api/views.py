from django.shortcuts import render

from rest_framework import generics
from .serializers import TripSerializer
from .models import Trip

class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = TripSerializer # tell django what serializer to use

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all().order_by('id')
    serializer_class = TripSerializer