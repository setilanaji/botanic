from django.urls import path
from plant.api.views import PlantView, GardenView, CategoryView
# from rest_framework.authtoken import views as authviews


urlpatterns = [
    path('species/', PlantView.as_view()),
    path('species/<slug:slug>/', PlantView.as_view()),
    path('garden/', GardenView.as_view()),
    path('garden/<slug:slug>/', GardenView.as_view()),
    path('category/', CategoryView.as_view()),
    # path('botanic/list/', BotanicView.as_view()),
    path('category/<slug:slug>/', CategoryView.as_view()),
    # path('botanic/detail/<int:id>/', BotanicView.as_view()),
]