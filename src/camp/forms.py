from django import forms
from .models import Camp, CampRegistration

class CampRegistrationForm(forms.ModelForm):
    camp = forms.ModelChoiceField(queryset=Camp.objects.all(), label='Camp', help_text='Select the camp you want to register for')

    class Meta:
        model = CampRegistration
        exclude = ('registration_date',)  # Exclude registration_date field from form
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