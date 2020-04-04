from rest_framework import serializers
from plant.models import Plant, Garden


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


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'desc',
            'date_added',
        )
        model = Garden
