from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from plant.models import Plant, Garden, Category
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import GardenSerializer, PlantSerializer, CategorySerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from plant.api.pagination import MyPagination


class PlantView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = PlantSerializer
    pagination_class = MyPagination
    queryset = Plant.objects.all()
    search_fields = ['name', ]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('gardens', 'categories')
    ordering_fields = ('gardens', 'name')
    lookup_field = 'slug'

    def get(self, request, slug=None):
        if slug:
            return self.retrieve(request)
        else:
            return self.list(request)


class GardenView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    # authentication_classes = TokenAuthentication
    # permission_classes = (IsAuthenticated,)
    serializer_class = GardenSerializer
    pagination_class = MyPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('plants',)
    ordering_fields = ('name',)
    queryset = Garden.objects.all()

    lookup_field = 'slug'

    def get(self, request, slug = None):
        if slug:
            return self.retrieve(request)
        else:
            return self.list(request)


class CategoryView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    # authentication_classes = TokenAuthentication
    # permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    pagination_class = MyPagination
    queryset = Category.objects.all()

    lookup_field = 'slug'

    def get(self, request, slug = None):
        if slug:
            return self.retrieve(request)
        else:
            return self.list(request)


# class BotanicView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
#     # authentication_classes = TokenAuthentication
#     # permission_classes = (IsAuthenticated,)
#     serializer_class = BotanicSerializer
#     pagination_class = MyPagination
#     queryset = Botanic.objects.all()
#
#     lookup_field = 'id'
#
#     def get(self, request, id = None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
