from rest_framework import serializers
from .models import Plant
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'family',
            'local',
            'synonym',
            'characteristic',
            'garden',
            'date_added',
        )
        model = Plant
