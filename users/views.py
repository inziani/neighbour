from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import redirect
from .models import UserProfile

from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'Signup.html'

class EditProfileView(UpdateView):
  model = UserProfile
  fields = ('first_name', 'middle_name', 'last_name', 'email', 'gok_id')
  template_name = 'edit_profile.html'
  success_url = reverse_lazy('home')
  



# Create your views here.
