# camps/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Camp, GeneralRegistration
from account.decorators import manager_required
from django.contrib.auth.decorators import login_required
from .forms import PlayerRegistrationForm, CoachRegistrationForm, ModifyPlayerRegistrationForm, ModifyCoachRegistrationForm, CampForm

def index(request):
    all_camps = Camp.objects.order_by('start_date')
    context = {'camps': all_camps}
    return render(request, 'camps/index.html', context)

def details(request, camp_id):
    try:
        camp = Camp.objects.get(pk=camp_id)
    except Camp.DoesNotExist:
        messages.error(request, 'This camp does not exist.')
        return render(request, 'f5rugby/error.html')
    
    context ={
        'camp': camp,
    }
    return render(request, 'camps/details.html', context)

@login_required
@manager_required
def create(request):
    if request.method == 'POST':
        form = CampForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('camps:manager_panel')
    else:
        form = CampForm()
    return render(request, 'camps/create.html', {'form': form})


def select_camp_role(request, camp_id):
    context = {
        'camp_id': camp_id,
    }
    return render(request, 'camps/select_role.html', context)

def register(request, camp_id, register_type):
    payment_link = ''
    template_name = ''
    camp = None
    type_string = ''
    
    # Check if camp exists
    try:
        camp = Camp.objects.get(pk=camp_id)
    except Camp.DoesNotExist:
        messages.error(request, 'This camp does not exist.')
        return render(request, 'f5rugby/error.html')

    # Get the registration type from query parameters
    if register_type not in ['player', 'coach']:
        messages.error(request, 'Invalid register type.')
        return render(request, 'f5rugby/error.html')

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
        if form.is_valid() and not request.POST.get('honeypot'):
            email = form.cleaned_data['email']
            # Check if there is already a registration with the same email under the same camp
            existing_registration = GeneralRegistration.objects.filter(camp=camp, email=email, type=register_type).exists()
            
            # Check for duplicate registration
            if existing_registration:
                messages.error(request, 'User with this email is already registered for this camp.')
            else:
                registration = form.save(commit=False)
                registration.camp = camp
                registration.type = register_type
                registration.save()
                return redirect('camps:register_success', payment_link=payment_link)
        else:
            messages.error(request, 'Ha! Bot.')
            return render(request, template_name, {'form': form})

    context = {
        'camp': camp,
        'type_string': type_string,
        'payment_link': payment_link,
        'form': form,
    }
    return render(request, template_name, context)

@login_required
@manager_required
def manager_panel(request):
    all_camps = Camp.objects.order_by('start_date')
    context = {
        'camps': all_camps,
    }
    return render(request, 'camps/manager/camp_list.html', context)


@login_required
@manager_required
def edit_registration(request, registration_id):
    try:
        registration = GeneralRegistration.objects.get(pk=registration_id)
    except GeneralRegistration.DoesNotExist:
        messages.error(request, 'This registrations does not exist.')
        return render(request, 'f5rugby/error.html')
    
    if registration.type == 'player':
        form_class = ModifyPlayerRegistrationForm
    elif registration.type == 'coach':
        form_class = ModifyCoachRegistrationForm
    else:
        messages.error(request, 'Unknown registration type.')
        return render(request, 'f5rugby/error.html')

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('accounts:camps_admin') 
    else:
        form = form_class(instance=registration)

    return render(request, 'camps/manager/edit_registration.html', {'form': form})

def register_success(request, payment_link):
    # Will require the camp, and the type of registeration
    # Player or coach, redirect to according payment
    context = {
        'payment_link': payment_link,
    }
    return render(request, 'camps/register_success.html', context)