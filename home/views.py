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
        
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "Tour packages retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                "message": "Tour package created successfully.",
                "tourPackage": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message": "Failed to create tour package.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class TourPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "message": "Tour package retrieved successfully.",
                "tourPackage": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Tour package not found.",
                "error": str(e)
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        try:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            if 'title' in request.data:
                serializer.save(slug=slugify(request.data['title']))
            else:
                serializer.save()
            return Response({
                "message": "Tour package updated successfully.",
                "tourPackage": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Failed to update tour package.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({
                "message": "Tour package deleted successfully."
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Failed to delete tour package.",
                "error": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)