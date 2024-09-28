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

class TourPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if 'title' in request.data:
            serializer.save(slug=slugify(request.data['title']))
        else:
            serializer.save()
        return Response(serializer.data)