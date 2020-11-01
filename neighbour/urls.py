from django.urls import path 
from .views import NeighbourListView
from . import views

urlpatterns = [
  path('', NeighbourListView.as_view(), name='neighbour')
  # path('', views.neighbourhood_list_view, name='neighbour')
]
