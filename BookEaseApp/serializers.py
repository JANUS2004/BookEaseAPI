from rest_framework import serializers
from .models import Bus, Flight

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['company_name', 'origin', 'destination', 'departure_time', 'arrival_time', 'price']

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['airline_name', 'origin', 'destination', 'departure_time', 'arrival_time', 'price']
