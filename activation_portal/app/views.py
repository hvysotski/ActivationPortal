from rest_framework import viewsets, request, mixins
from rest_framework.response import Response
from .models import ActivationCode
from .serializers import ActivationCodeSerializer


class ActivationCodeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for viewing and editing activation codes.
    """
    serializer_class = ActivationCodeSerializer
    queryset = ActivationCode.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data_dict = serializer.data
        instance.delete()
        return Response(data_dict)
