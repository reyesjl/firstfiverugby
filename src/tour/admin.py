from django.contrib import admin
from .models import TourQuote

class TourQuoteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'club_name', 'status')
    list_filter = ('status',)

admin.site.register(TourQuote, TourQuoteAdmin)