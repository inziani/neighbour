from django.urls import path 
from .views import NeighbourListView, SearchResultsListView, CreateConvoView, BusinessListView, ConversationListView
from . import views

urlpatterns = [
  path('', NeighbourListView.as_view(), name='neighbour'),
  path('business/', BusinessListView.as_view(), name='business'),
  path('conversation/', ConversationListView.as_view(), name='conversation'),
  path('', NeighbourListView.as_view(), name='neighbour'),
  path('search/', SearchResultsListView.as_view(), name ='search_results'),
  path('new/', CreateConvoView.as_view(), name='new_convo'),
  # path('', views.neighbourhood_list_view, name='neighbour')
]
