from django.contrib import admin
from django.contrib.auth.admin import Group, UserAdmin
from .models import Tarqatuvchi


class TarqatuvchiAdmin(UserAdmin):
    fieldsets = (
        ('Login', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bolim', 'manzil', 'tel')}),
    )
    list_display = ('username', 'bolim', 'tel', 'manzil')


admin.site.unregister(Group)
admin.site.register(Tarqatuvchi, TarqatuvchiAdmin)
