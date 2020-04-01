from django.shortcuts import render
from . import models
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from . import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ListPlant(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Plant.objects.all()
    serializer_class = serializers.PlantSerializer


class DetailPlant(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Plant.objects.all()
    serializer_class = serializers.PlantSerializer
