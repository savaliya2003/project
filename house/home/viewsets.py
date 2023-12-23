from rest_framework import viewsets
from . import models
from . import serializers

class HomeViewset(viewsets.ModelViewSet):
    queryset = models.Home.objects.all()
    serializer_class = serializers.HomeSerializer