from django.contrib import admin
from .models import Camp

class CampAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title',)  # Enable search by camp name
    list_filter = ('tags',)  # Enable filtering by tags

admin.site.register(Camp, CampAdmin)