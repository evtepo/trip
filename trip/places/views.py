from django.shortcuts import render
from rest_framework import generics
from .serializers import HotelsSerializer
from .models import *


class HotelsAPIView(generics.ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer