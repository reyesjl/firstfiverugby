from django import forms
from .models import FitnessEvaluation

class FitnessEvaluationForm(forms.ModelForm):
    class Meta:
        model = FitnessEvaluation
        fields = ['first_name', 'last_name', 'email', 'phone', 'workout_or_meal_plan', 'goals_description']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
            'workout_or_meal_plan': 'Upload Your Current Workout or Meal Plan',
            'goals_description': 'Describe Your Fitness Goals',
        }
        help_texts = {
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'email': 'Enter your email address',
            'phone': 'Enter your phone number',
            'workout_or_meal_plan': 'Upload a file (PDF, image, etc.) of your current workout or meal plan',
            'goals_description': 'Describe your fitness goals and any specific requirements you have',
        }