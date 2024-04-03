from django.contrib import admin
from .models import Camp, CampRegistration, CoachCampRegistration

class CampAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title',)  # Enable search by camp name
    list_filter = ('tags',)  # Enable filtering by tags

class CampRegistrationAdmin(admin.ModelAdmin):
    list_display = ('player_first_name', 'player_last_name', 'camp', 'registration_date')
    list_filter = ('camp', 'registration_date')
    search_fields = ('player_first_name', 'player_last_name', 'camp__title')

class CoachCampRegistrationAdmin(admin.ModelAdmin):
    list_display = ('coach_first_name', 'coach_last_name', 'camp', 'registration_date')
    list_filter = ('camp', 'registration_date')
    search_fields = ('coach_first_name', 'coach_last_name', 'camp__title')

admin.site.register(Camp, CampAdmin)
admin.site.register(CampRegistration, CampRegistrationAdmin)
admin.site.register(CoachCampRegistration, CoachCampRegistrationAdmin)
