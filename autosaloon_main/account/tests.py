import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

# Create your tests here.
class AddSaloon_TestCase(APITestCase):

    def test_add_user(self):

        saloondata = {
        # "id": 1,
        "email": "ainae06@gmail.com",
        "name": "John",
        "phonenumber": "09012332233",
        "address": "3, Ade Street, Ojota Lagos."
        }

        create_response = self.client.post('/api/view/saloon/edit/', saloondata)

        data =  {
        "email": "admin@gmail.com",
        "firstname": "admin",
        "lastname": "user",
        "password": "admin12343",
        "gebnder": 'Male',
        "phone": "09011223344",
        "roles": "Customer",
        "is_staff": 'false',
        "saloon": "http://127.0.0.1:8000/api/view/saloon/edit/1/"
        }
        

        create_response = self.client.post('/api/account/register/', data)

        if create_response.status_code == 201:
            print('Created Account Successfully')
        else:
            print(create_response.content)
        
        # print(dir(create_response))
        return self.assertEqual(create_response.status_code,status.HTTP_201_CREATED)

