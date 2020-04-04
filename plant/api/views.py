from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from plant.models import Plant, Garden
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import GardenSerializer, PlantSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class PlantView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PlantSerializer
    pagination_class = PageNumberPagination
    queryset = Plant.objects.all()
    search_fields = ['name', ]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('garden',)
    ordering_fields = ('garden', 'name')
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)


class GardenView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = TokenAuthentication
    permission_classes = (IsAuthenticated,)
    serializer_class = GardenSerializer
    pagination_class = PageNumberPagination
    queryset = Garden.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)