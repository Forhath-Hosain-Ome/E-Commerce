from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'is_admin', 'is_superuser', 'username', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account)