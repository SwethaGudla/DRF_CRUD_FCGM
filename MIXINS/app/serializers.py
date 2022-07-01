from concurrent.futures.process import _system_limits_checked
from app.models import StdModel
from rest_framework import serializers
class StdSerializer(serializers.ModelSerializer):
    class Meta:
        model = StdModel
        fields = "__all__"