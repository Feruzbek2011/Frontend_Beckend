from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUsersChangingForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUsersChangingForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'is_staff'] # bular adminda ko'rinadigan narsalar.
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    ) # bu yoshin ham belgilash mumkin qiladi.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    ) # buni nima ekanligini bilmayman.

admin.site.register(CustomUser, CustomUserAdmin)
