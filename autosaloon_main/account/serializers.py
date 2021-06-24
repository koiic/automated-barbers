from rest_framework import serializers
from django.contrib.auth import get_user_model
from account.models import CustomUser
from email_validator import validate_email, EmailNotValidError
from django.utils.crypto import get_random_string
from django.conf import settings

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['last_login', 'date_joined', 'is_superuser', 'groups', 'user_permissions']
        extra_kwargs = {'password':{'write_only' :True}}

    def create(self, validated_data):
        extra_fields = {
            'firstname':validated_data['firstname'], 
            'gender':validated_data['gender'],
            'phone':validated_data['phone'],
            'roles':validated_data['roles'],
            'is_staff':validated_data['is_staff'],
            'saloon':validated_data['saloon'],
        }
        user = CustomUser.objects.create_user(
            validated_data['email'], 
            validated_data['password'],
            **extra_fields,)

        return user

