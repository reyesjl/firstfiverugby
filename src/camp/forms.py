from django import forms
from .models import Camp, CampRegistration, CoachCampRegistration

from django import forms
from .models import Camp, CampRegistration, CoachCampRegistration

class CampRegistrationForm(forms.ModelForm):
    camp = forms.ModelChoiceField(queryset=Camp.objects.all(), label='Camp', help_text='Select the camp you want to register for')

    class Meta:
        model = CampRegistration
        fields = ['camp', 'player_first_name', 'player_last_name', 'player_birthday', 'player_club', 'player_position', 'emergency_contact_first_name', 'emergency_contact_last_name', 'emergency_contact_email', 'emergency_contact_phone', 'photo_release_form', 'liability_waiver']
        labels = {
            'player_first_name': 'Player First Name',
            'player_last_name': 'Player Last Name',
            'player_birthday': 'Date of Birth',
            'player_club': 'Club',
            'player_position': 'Position',
            'emergency_contact_first_name': 'Emergency Contact First Name',
            'emergency_contact_last_name': 'Emergency Contact Last Name',
            'emergency_contact_email': 'Emergency Contact Email',
            'emergency_contact_phone': 'Emergency Contact Phone',
            'photo_release_form': 'Photo Release Form',
            'liability_waiver': 'Liability Waiver',
        }
        help_texts = {
            'player_first_name': 'Enter your first name',
            'player_last_name': 'Enter your last name',
            'player_birthday': 'Enter your date of birth',
            'player_club': 'Enter your club name',
            'player_position': 'Enter your playing position',
            'emergency_contact_first_name': 'Enter emergency contact first name',
            'emergency_contact_last_name': 'Enter emergency contact last name',
            'emergency_contact_email': 'Enter emergency contact email',
            'emergency_contact_phone': 'Enter emergency contact phone',
            'photo_release_form': 'Upload photo release form (PDF)',
            'liability_waiver': 'Upload liability waiver (PDF)',
        }
        widgets = {
            'player_birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class CoachCampRegistrationForm(forms.ModelForm):
    camp = forms.ModelChoiceField(queryset=Camp.objects.all(), label='Camp', help_text='Select the camp you want to register for')

    class Meta:
        model = CoachCampRegistration
        fields = ['camp', 'coach_first_name', 'coach_last_name', 'coach_email', 'coach_phone', 'coach_club']
        labels = {
            'coach_first_name': 'First Name',
            'coach_last_name': 'Last Name',
            'coach_email': 'Email',
            'coach_phone': 'Phone Number',
            'coach_club': 'Club',
        }
        help_texts = {
            'coach_first_name': 'Enter your first name.',
            'coach_last_name': 'Enter your last name.',
            'coach_email': 'Enter your email address.',
            'coach_phone': 'Enter your phone number.',
            'coach_club': 'Enter the name of your club.',
        }
