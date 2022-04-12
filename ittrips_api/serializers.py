from rest_framework import serializers 
from .models import Trip 

class TripSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model =Trip # tell django which model to use
        fields = ('name', 'duration', 'overview','activities') # tell django which fields to include