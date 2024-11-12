from django.contrib import admin
from .models import Contacts, Opens


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'tariff', 'email', 'number', 'time_create')
    list_display_links = ('name', 'city', 'tariff', 'email', 'number', 'time_create')
    search_fields = ('name', 'city', 'email', 'number')
    list_filter = ('name', 'city', 'email', 'number', 'time_create')

class OpensAdmin(admin.ModelAdmin):
    list_display = ('ip', 'time_create')
    list_display_links = ('ip', 'time_create')
    search_fields = ('ip',)
    list_filter = ('ip', 'time_create')

admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Opens, OpensAdmin)