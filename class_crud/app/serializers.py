from rest_framework import serializers
from app.models import Task
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"