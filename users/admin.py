from django.contrib import admin
from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

class UserProfileInLine(admin.StackedInline):
  model = UserProfile
  can_delete = False
  verbose_plural_name = 'User Profile'
  fk_name = 'user'

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ['email', 'username','date_joined', 'user_type']
  inlines = (UserProfileInLine,)

  
admin.site.register(CustomUser, CustomUserAdmin)
