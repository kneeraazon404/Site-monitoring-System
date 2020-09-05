from rest_framework import serializers
from .models import Cement

# Using  ModelSerializer


class CementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cement
        fields = "__all__"
