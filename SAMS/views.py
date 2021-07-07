from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .models import Account, Student, Professor,  Image
from .serializers import StudentSerializer, AccountSerializer, ProfessorSerializer,  ImageSerializer

from rest_framework import request
from rest_framework.response import Response
from rest_framework.decorators import api_view


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

#
# class YEARViewSet(viewsets.ModelViewSet):
#     queryset = YEAR.objects.all()
#     serializer_class = YEARSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
