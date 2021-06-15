from .models import Saloon

from rest_framework import serializers

class SaloonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saloon
        fields = ('id', 'name', 'email', 'phonenumber', 'address')