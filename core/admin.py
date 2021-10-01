from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUser

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUser):
    ordering= ['id']    ## The value of 'ordering' must be a list or tuple.
    list_display= ['id', 'username', 'email']
    list_display_links= ['id', 'username', 'email']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal_Info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff')}),
        ('Important_Dates', {'fields': ('last_login',)}),
    )
    ## fieldsets is a Tuple carries Tuples , each tuple is divided into 2 parts .. General Title  // Dictionary.
    add_fieldsets= (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
            }
         ),
         )