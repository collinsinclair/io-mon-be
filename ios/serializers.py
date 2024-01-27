from rest_framework import serializers
from .models import *


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Input
        fields = ["id", "name"]


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    inputs = InputSerializer(many=True, read_only=True)

    class Meta:
        model = Output
        fields = ["id", "name", "inputs"]


class AskSerializer(serializers.HyperlinkedModelSerializer):
    input = InputSerializer(many=False, read_only=True)
    output = OutputSerializer(many=False, read_only=True)

    class Meta:
        model = Ask
        fields = ["id", "output", "input", "value", "done", "created_at"]
