from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bus, Flight
from .serializers import BusSerializer, FlightSerializer

class BusList(APIView):
    def get(self, request, origin, destination):
        try:
            buses = Bus.objects.get(origin=origin,destination=destination)
            serializer = BusSerializer(buses)
            print('The Data')
            print(serializer.data)
            return Response(serializer.data)
        except Bus.DoesNotExist:
            return Response({"message": "No buses for the given cxlocation"}, status=status.HTTP_404_NOT_FOUND)
   

class FlightList(APIView):
    def get(self, request, origin, destination):
        try:
            flights = Flight.objects.get(origin=origin,destination=destination)
            serializer = FlightSerializer(flights)
            print('The Data')
            print(serializer.data)
            return Response(serializer.data)
        except Flight.DoesNotExist:
            return Response({"message": "No flights for the given location"}, status=status.HTTP_404_NOT_FOUND)
   
    