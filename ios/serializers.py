from rest_framework import serializers
from .models import *


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Input
        fields = ["name"]


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Output
        fields = ["name", "inputs"]


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    # created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Request
        fields = ["output", "input", "value", "done", "created_at"]
