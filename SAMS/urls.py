from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, AccountViewSet, ProfessorViewSet, ImageViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('student', StudentViewSet, basename='student')
router.register('account', AccountViewSet, basename='account')
router.register('professor', ProfessorViewSet, basename='professor')
# router.register('materialsoftheyear', YEARViewSet, basename='materialsoftheyear')
router.register('Image', ImageViewSet, basename='Image')


urlpatterns = [
    path('', include(router.urls)),
]

















