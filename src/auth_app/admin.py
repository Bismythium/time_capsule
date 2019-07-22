from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auth_app.forms import CustomUserCreationForm, CustomUserChangeForm
from auth_app.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username',]

admin.site.register(CustomUser,CustomUserAdmin)
