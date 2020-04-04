from django.urls import path
from plant.api.views import PlantView, GardenView
# from rest_framework.authtoken import views as authviews


urlpatterns = [
    path('list/', PlantView.as_view()),
    path('detail/<int:id>/', PlantView.as_view()),
    path('garden/list/', GardenView.as_view()),
    path('garden/detail/<int:id>/', GardenView.as_view()),
]