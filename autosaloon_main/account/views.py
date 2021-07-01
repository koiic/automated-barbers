from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from .models import  CustomUser
from .serializers import CreateUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from decouple import config


class RegisterView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer


# class LoginView(APIView):
#     permission_classes = (AllowAny,)
#     ### Login to create token after Registration

#     def post(self, request):
#         ### Login Using Email and Password
#         email = request.data['email']
#         password = request.data['password']

#         ### Authenticate the User
#         user = CustomUser.objects.filter(email=email).first()
#         if user is None:
#             raise AuthenticationFailed("user not found")
#         if not user.check_password(password):
#             raise AuthenticationFailed("Incorrect Password")


#         ### Generate T0ken
#         payload = {
#             "id":user.id,
#             "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             "iat":datetime.datetime.utcnow()
#         }
#         token = jwt.encode(payload, config("secretKey"), algorithm='HS256')
#         payload['token'] = token

#         ### Add token to cookie so it can be accessed across the app
#         response = Response()
#         response.set_cookie(key='token', value=token, httponly=True)
#         response.data = payload
        

#         return response

# Not in use at the moment
class LogoutView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        
        ### Logout Views

        # Check if any user is currently Logged in
        token = request.COOKIES.get('token')
        if not token:
            raise AuthenticationFailed("No User Currently Logged in")
        
        # Delete Saved Login Detail from Cookies
        else:
            response = Response()
            response.delete_cookie('token')

            response.data = {
                "message":"Logout Successful"
                }

        return response

