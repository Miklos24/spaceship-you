from django.shortcuts import render
from .models import ZoneTimes
from .serializers import ZoneSerializer
from rest_framework import generics

# Create your views here.
class ZoneListCreate(generics.ListCreateAPIView):
    queryset = ZoneTimes.objects.all()
    serializer_class = ZoneSerializer
