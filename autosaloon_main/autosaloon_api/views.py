import jwt
from decouple import config
from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Saloon
from .serializers import SaloonSerializer


class SaloonView(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin
    ):
    
    ### This view allows any user to see the list of available saloons
    permission_classes = (AllowAny,)

    serializer_class = SaloonSerializer
    queryset = Saloon.objects.all()

class SaloonEdit(
    viewsets.GenericViewSet, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    ):  

    
    permission_classes = (AllowAny,)# Only staff can update, delete or create new saloon: If user.is_staff = True

    serializer_class = SaloonSerializer
    queryset = Saloon.objects.all()


