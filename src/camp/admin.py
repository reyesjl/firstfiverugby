from django.contrib import admin
from .models import Camp, GeneralRegistration

class CampAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title',)  # Enable search by camp name
    list_filter = ('tags',)  # Enable filtering by tags

class GeneralRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'type', 'camp','has_paid')
    list_filter = ('type', 'camp', 'has_paid')
    search_fields = ('first_name', 'last_name', 'phone', 'emergency_phone', 'email', 'emergency_email')

admin.site.register(Camp, CampAdmin)
admin.site.register(GeneralRegistration, GeneralRegistrationAdmin)
