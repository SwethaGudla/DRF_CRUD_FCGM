from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Employee(APIView):
    def get(self,request):
        emp = Task.objects.all()
        serializer = TaskSerializers(emp,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmpoloyeeUpdate(APIView):

    def get(self,request,pk):
        emp=Task.objects.get(id=pk)
        serializers=TaskSerializers(emp)
        return Response(serializers.data)

    def put(self,request,pk):
        emp=Task.objects.get(id=pk)
        serializers=TaskSerializers(instance=emp,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        emp=Task.objects.get(id=pk)
        emp.delete()
        return Response("item deleted successfully..!")



