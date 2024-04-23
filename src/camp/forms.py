from django import forms
from .models import GeneralRegistration

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
