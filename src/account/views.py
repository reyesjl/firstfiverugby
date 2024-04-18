from django.db.models import Q
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from .decorators import manager_required
from django.shortcuts import render, redirect
from camp.models import Camp, GeneralRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        honeypot = request.POST.get('honeypot', '')
        password = request.POST.get('password', '')

        if form.is_valid() and not honeypot:
            form.save()
            return render(request, 'accounts/signup_success.html')
        else:
            if honeypot:
                error_message = 'Alert: Bot detected! This incident will be reported to the administrator.'
                messages.error(request, error_message)
            else:
                error_message = 'Correct the errors below.'
                messages.error(request, error_message)
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)

def logon(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)

def logoff(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):
    user = request.user

    context = {
        'motd': 'Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.',
    }
    
    # Check if the user belongs to a specific group
    if user.groups.filter(name='Manager').exists():
        return render(request, 'accounts/admin_dashboard.html', context)
    elif user.groups.filter(name='Trainer').exists():
        return render(request, 'accounts/trainer_dashboard.html', context)
    else:
        return render(request, 'accounts/default_dashboard.html', context)

@login_required
@manager_required
def camps_summary(request):
    registrations = GeneralRegistration.objects.all()

    # Filter by search query
    search_query = request.GET.get('search')
    if search_query:
        registrations = registrations.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    # Filter by type
    type_filter = request.GET.get('type')
    if type_filter:
        registrations = registrations.filter(type=type_filter)

    # Filter by paid status
    paid_filter = request.GET.get('paid')
    if paid_filter in ['true', 'false']:
        registrations = registrations.filter(has_paid=(paid_filter == 'true'))

    # Calculate revenue and other statistics
    total_revenue = 0
    total_coaches = 0
    total_players = 0
    for registration in registrations:
        if registration.type == 'coach':
            total_revenue += 100
            total_coaches += 1
        elif registration.type == 'player':
            total_revenue += 325
            total_players += 1

    context = {
        'registrations': registrations,
        'total_revenue': total_revenue,
        'total_players': total_players,
        'total_coaches': total_coaches,
    }
    return render(request, 'accounts/camps_summary.html', context)