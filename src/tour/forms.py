from django import forms
from .models import TourQuote

class TourQuoteForm(forms.ModelForm):
    class Meta:
        model = TourQuote
        fields = ['first_name', 'last_name', 'club_name', 'club_size', 'contact_email', 'phone_number']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'club_name': 'Club Name',
            'club_size': 'Club Size',
            'contact_email': 'Contact Email',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'club_size': 'Enter the number of members in your club.',
            'contact_email': 'Please provide a valid email address.',
            'phone_number': 'Enter your phone number including country code if applicable.',
        }
