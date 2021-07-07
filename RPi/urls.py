from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import Image_Create, Image_List

router = routers.DefaultRouter()
# router.register('student', StudentViewSet, basename='student')
urlpatterns = [
    path('image_create', Image_Create.as_view() ),
path('image_list', Image_List.as_view()),
]