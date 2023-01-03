from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import CastSerializer
from .models import Cast

class CastList(generics.ListCreateAPIView):
    queryset = Cast.objects.all().order_by('id')
    serializer_class = CastSerializer

class CastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cast.objects.all().order_by('id')
    serializer_class = CastSerializer