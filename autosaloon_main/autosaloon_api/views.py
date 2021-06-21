from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Saloon
from .serializers import SaloonSerializer
from decouple import config

class Saloon(viewsets.ModelViewSet):
    # Create your views here.
    queryset = Saloon.objects.all()
    serializer_class = SaloonSerializer
