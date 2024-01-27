from rest_framework import permissions, viewsets
from .serializers import *
from .models import *


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

    queryset = Request.objects.all().order_by("created_at")
    serializer_class = RequestSerializer
