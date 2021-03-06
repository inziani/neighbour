from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .models import Neighbourhood, Business, Conversation

# Create your views here.

class CreateConvoView(CreateView):
  model = Conversation
  template_name = 'conversation.html'
  fields = ('topic', 'details', 'member')
  
  
  

# def neighbourhood_list_view(request): 
#   business = Business.objects.all()
#   neighbourhood = Neighbourhood.objects.all()
#   return render(request, 'neighbour.html', {'Neighbourhood':neighbourhood, 'Business':business})

class NeighbourListView(ListView):
  model = Neighbourhood 
  template_name = 'neighbour.html'

class BusinessListView(ListView):
  model = Business 
  template_name = 'biashara.html'

class ConversationListView(ListView):
  model = Conversation 
  template_name = 'moshene.html'

# class NeighbourListView(ListView):
#   # context_object_name = 'list'    
#   template_name = 'neighbour.html'
#   queryset= Neighbourhood.objects.all()

# def get_context_data(self, **kwargs):
#     business= Business.objects.all()
#     neighbourhood = Business.objects.all()
#     conversation = Conversation.object.all()
#     context = {
#       'business':business, 
#       'neighbourhood':neighbourhood,
#       'conversation':conversation,
#     }
#     return context

class SearchResultsListView(ListView):
  model = Business
  template_name = 'neighbour.html'

  def get_queryset(self):
    query = self.request.GET.get('q')
    return Business.objects.filter(Q(name__icontains=query)| Q(business_type__icontains=query))






