from django import forms
from .models import GeneralRegistration, Camp

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ['title', 'address', 'description', 'start_date', 'end_date', 'tags', 'details', 'crest', 'coach_price', 'player_price', 'coach_payment_link', 'player_payment_link']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PlayerRegistrationForm(forms.ModelForm):
    class Meta:
        model = GeneralRegistration
        fields = ['first_name', 'last_name', 'email', 'club', 'position', 'birthday', 'emergency_contact_first_name', 'emergency_contact_last_name', 'emergency_contact_email', 'emergency_contact_phone', 'photo_release_form', 'liability_waiver']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class CoachRegistrationForm(forms.ModelForm):
    class Meta:
        model = GeneralRegistration
        fields = ['first_name', 'last_name', 'email', 'phone', 'club', 'photo_release_form', 'liability_waiver']

class ModifyPlayerRegistrationForm(forms.ModelForm):
    class Meta:
        model = GeneralRegistration
        fields = ['first_name', 'last_name', 'email', 'club', 'position', 'birthday', 'emergency_contact_first_name', 'emergency_contact_last_name', 'emergency_contact_email', 'emergency_contact_phone', 'has_paid']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class ModifyCoachRegistrationForm(forms.ModelForm):
    class Meta:
        model = GeneralRegistration
        fields = ['first_name', 'last_name', 'email', 'phone', 'club', 'has_paid']
