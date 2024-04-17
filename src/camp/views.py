# camps/views.py
from django.shortcuts import render, redirect
from .models import Camp, GeneralRegistration
from .forms import PlayerRegistrationForm, CoachRegistrationForm, CampRegistrationForm, CoachCampRegistrationForm

def index(request):
    all_camps = Camp.objects.order_by('start_date')
    context = {'camps': all_camps}
    return render(request, 'camps/index.html', context)

def select_camp_role(request, camp_id):
    context = {
        'camp_id': camp_id,
    }
    return render(request, 'camps/select_role.html', context)

def register(request, camp_id, register_type):
    error_message = ''
    payment_link = ''
    template_name = ''
    camp = None
    type_string = ''
    
    # Check if camp exists
    try:
        camp = Camp.objects.get(pk=camp_id)
    except Camp.DoesNotExist:
        error_message = "This camp does not exist."
        return render(request, 'camps/error.html', error_message)

    # Get the registration type from query parameters
    if register_type not in ['player', 'coach']:
        error_message = "Invalid register type."
        return render(request, 'camps/error.html', {'error_message': error_message})

    # Determine the form based on the registration type
    if register_type == 'player':
        form = PlayerRegistrationForm(request.POST or None)
        payment_link = camp.player_payment_link
        template_name = 'camps/register_player.html'
        type_string = 'players'
    elif register_type == 'coach':
        form = CoachRegistrationForm(request.POST or None)
        payment_link = camp.coach_payment_link
        template_name = 'camps/register_coach.html'
        type_string = 'coaches'

    # Process form
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if there is already a registration with the same email under the same camp
            existing_registration = GeneralRegistration.objects.filter(camp=camp, email=email, type=register_type).exists()
            
            # Check for duplicate registration
            if existing_registration:
                error_message = "User with this email is already registered for this camp."
            else:
                registration = form.save(commit=False)
                registration.camp = camp
                registration.type = register_type
                registration.save()
                return redirect('camps:register_success', payment_link=payment_link)

    context = {
        'error_message': error_message,
        'camp': camp,
        'type_string': type_string,
        'payment_link': payment_link,
        'form': form,
    }
    return render(request, template_name, context)

def register_success(request, payment_link):
    # Will require the camp, and the type of registeration
    # Player or coach, redirect to according payment
    context = {
        'payment_link': payment_link,
    }
    return render(request, 'camps/register_success.html', context)