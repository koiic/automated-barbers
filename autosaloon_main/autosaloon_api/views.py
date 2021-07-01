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

# @api_view(['GET'])
# def cookie(self, request):
#     token = request.COOKIES.get('token')

#     # Check if token exists
#     if not token:
#         raise AuthenticationFailed('Login required to access this page')

#     # Decode token
#     try:
#         payload = jwt.decode(token, config('secretKey'), algorithms=['HS256'])
#     except jwt.ExpiredSignatureError:
#         raise AuthenticationFailed('Expired token: Please login and try again. ')
    
#     return Response(None)

class SaloonEdit(
    viewsets.GenericViewSet, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    ):  

    
    permission_classes = (IsAdminUser,)# Only staff can update, delete or create new saloon: If user.is_staff = True

    serializer_class = SaloonSerializer
    queryset = Saloon.objects.all()


