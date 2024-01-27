from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


class InputViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Inputs to be viewed or edited.
    """

    queryset = Input.objects.all().order_by("name")
    serializer_class = InputSerializer


class OutputViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Outputs to be viewed or edited.
    """

    queryset = Output.objects.all().order_by("name")
    serializer_class = OutputSerializer


class AskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Asks to be viewed or edited.
    """

    queryset = Ask.objects.all().order_by("-created_at")
    serializer_class = AskSerializer

    @action(detail=False)
    def open(self, request):
        asks = Ask.objects.filter(done=False).order_by("-created_at")
        serializer = self.get_serializer(asks, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def mark_as_done(self, request, pk=None):
        ask = self.get_object()
        ask.done = True
        ask.save()
        return Response({"status": "Ask marked as done"})
