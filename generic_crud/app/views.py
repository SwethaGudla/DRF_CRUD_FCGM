from operator import ge
from django.shortcuts import render
from app.models import EmployeeData
from app.serializer import Emp_Serializer
from rest_framework import generics
# Create your views here.
class EmployeeCreateGenerics(generics.CreateAPIView):
    queryset=EmployeeData.objects.all()
    serializer_class = Emp_Serializer

class EmployeeListGenerics(generics.ListAPIView):
    queryset=EmployeeData.objects.all()
    serializer_class = Emp_Serializer

class EmployeeDetailGenerics(generics.RetrieveAPIView,
                            generics.UpdateAPIView,
                            generics.DestroyAPIView):
    queryset=EmployeeData.objects.all()
    serializer_class = Emp_Serializer

class EmployeeListCreateGenerics(generics.ListCreateAPIView):
    queryset=EmployeeData.objects.all()
    serializer_class = Emp_Serializer

class EmployeeAllGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmployeeData.objects.all()
    serializer_class = Emp_Serializer

