from home.models import *
from rest_framework import serializers

class TourPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = '__all__'