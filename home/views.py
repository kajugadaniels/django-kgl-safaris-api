from home.models import *
from home.serializers import *
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class TourPackageListCreateView(generics.ListCreateAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        slug = slugify(title)
        serializer.save(slug=slug)