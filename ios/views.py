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


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Requests to be viewed or edited.
    """

    queryset = Request.objects.all().order_by("-created_at")
    serializer_class = RequestSerializer

    @action(detail=False)
    def open_requests(self, request):
        requests = Request.objects.filter(done=False).order_by("-created_at")
        serializer = self.get_serializer(requests, many=True)
        return Response(serializer.data)
