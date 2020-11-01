from django.shortcuts import render
from django.views.generic import ListView

from .models import Neighbourhood, Business, Conversation

# Create your views here.

# def neighbourhood_list_view(request): 
#   business = Business.objects.all()
#   neighbourhood = Neighbourhood.objects.all()
#   return render(request, 'neighbour.html', {'Neighbourhood':neighbourhood, 'Business':business})

class NeighbourListView(ListView):
  model = Business 
  template_name = 'neighbour.html'

# class NeighbourListView(ListView):
#   # context_object_name = 'object'    
#   template_name = 'neighbour.html'
#   queryset= Neighbourhood.objects.all()

# def get_context_data(self, **kwargs):
#     context = super(NeighbourListView, self).get_context_data(**kwargs)
#     context['business'] = Business.objects.all()
#     context['neighbourhood'] = self.queryset
#     return context


