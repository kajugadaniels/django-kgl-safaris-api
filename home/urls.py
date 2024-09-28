from django.urls import path
from django.conf import settings
from home.views import *
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('tour-packages/', TourPackageListCreateView.as_view(), name='tourpackageListCreate'),
    path('tour-packages/<slug:slug>/', TourPackageDetailView.as_view(), name='tourpackageDetail'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)