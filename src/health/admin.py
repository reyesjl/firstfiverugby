from django.contrib import admin
from .models import FitnessEvaluation, HealthPlan

class FitnessEvaluationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

class HealthPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'plan_type')
    search_fields = ('title', 'author', 'plan_type')

admin.site.register(FitnessEvaluation, FitnessEvaluationAdmin)
admin.site.register(HealthPlan, HealthPlanAdmin)
