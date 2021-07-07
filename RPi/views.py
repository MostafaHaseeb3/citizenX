from django.shortcuts import render
from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer

# Create your views here.


class Image_Create(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class Image_List(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

