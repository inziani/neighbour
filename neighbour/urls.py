from django.urls import path 
from .views import NeighbourListView, SearchResultsListView
from . import views

urlpatterns = [
  path('', NeighbourListView.as_view(), name='neighbour'),
  path('search/', SearchResultsListView.as_view(), name ='search_results'),
  # path('', views.neighbourhood_list_view, name='neighbour')
]
