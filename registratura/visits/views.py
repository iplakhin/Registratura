from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Visit
from .serializers import *


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']

        if not pk:
            return Visit.objects.all()[:5]
        return Visit.objects.filter(pk=pk)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
