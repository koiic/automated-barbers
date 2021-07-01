from .models import Saloon

from rest_framework import serializers

class SaloonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Saloon
        fields = '__all__'
