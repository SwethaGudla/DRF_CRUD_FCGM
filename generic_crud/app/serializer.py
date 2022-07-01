from rest_framework import serializers
from app.models import EmployeeData
class Emp_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeData
        fields = "__all__"