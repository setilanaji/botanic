from django.forms import model_to_dict
from rest_framework import serializers
from plant.models import Plant, Garden, Category, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'imagefile'
        )
        model = Photo


class PlantSerializerRelated(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            'image',
        )
        model = Plant


class CategorySerializerRelated(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, data):
        return {
            'id': data.id,
            'slug': data.slug,
            'name': data.name,
        }


class CategorySerializer(serializers.ModelSerializer):
    plants = PlantSerializerRelated(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'slug',
            'name',
            'description',
            'plants',
            'image',
            'date_added',
        )
        model = Category


class GardenSerializerRelated(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, data):
        return {
            'id': data.id,
            'slug': data.slug,
            'name': data.name,
        }


class PlantSerializer(serializers.ModelSerializer):
    categories = CategorySerializerRelated(many=True, read_only=True)
    gardens = GardenSerializerRelated(many=True, read_only=True)
    more_photos = PhotoSerializer(many=True, read_only= True)

    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            # 'family',
            'local',
            'more_photos',
            'synonym',
            'image',
            'characteristic',
            'gardens',
            'categories',
            'date_added',
        )
        model = Plant


class GardenSerializer(serializers.ModelSerializer):
    plants = PlantSerializerRelated(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'slug',
            'name',
            'desc',
            'location_long',
            'location_lat',
            'image',
            'date_added',
            'plants',
            # 'botanic',
        )
        model = Garden


