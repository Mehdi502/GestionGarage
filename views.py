from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView

from .models import Car
from .serializers import CarSerializer

# Create your views here.
class CarDetailAPIView(APIView):
    def get(self, request, immatriculation):
        car = get_object_or_404(Car, immatriculation=immatriculation)
        serializer = CarSerializer(car)
        return Response(serializer.data)

class CarListCreateAPIView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateAPIView(APIView):
    def put(self, request, immatriculation):
        car = get_object_or_404(Car, immatriculation=immatriculation)
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDeleteAPIView(APIView):
    def delete(self, request, immatriculation):
        car = get_object_or_404(Car, immatriculation=immatriculation)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
