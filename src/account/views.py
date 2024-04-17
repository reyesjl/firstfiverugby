from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        honeypot = request.POST.get('honeypot', None)
        password = request.POST.get('password', None)

        if form.is_valid() and not honeypot:
            form.save()
            return render(request, 'accounts/signup_success.html')
        else:
            if honeypot:
                error_message = 'Alert: Bot detected! This incident will be reported to the administrator.'
            elif len(password) < 8:
                error_message = 'Password must be at least 8 characters long.'
            elif password.isdigit():
                error_message = 'Password cannot be fully numeric.'
            else:
                error_message = 'Please correct the errors below.'
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