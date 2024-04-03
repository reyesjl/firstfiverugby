# camps/views.py
from django.shortcuts import render, redirect
from .models import Camp
from .forms import CampRegistrationForm, CoachCampRegistrationForm

def index(request):
    all_camps = Camp.objects.order_by('start_date')
    context = {'camps': all_camps}
    return render(request, 'camps/index.html', context)

# Coach link: https://buy.stripe.com/aEU9Bp1Q75oWeGs003
# Player link: https://buy.stripe.com/8wM14TbqH4kSfKw7su
def register_for_camp(request):
    if request.method == 'POST':
        form = CampRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to payment page
            return redirect('https://buy.stripe.com/8wM14TbqH4kSfKw7su')
    else:
        form = CampRegistrationForm()
    
    return render(request, 'camps/register_camp.html', {'form': form})

def register_for_camp_as_coach(request):
    if request.method == 'POST':
        form = CoachCampRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the coach payment page
            return redirect('https://buy.stripe.com/aEU9Bp1Q75oWeGs003')
    else:
        form = CoachCampRegistrationForm()
    
    return render(request, 'camps/register_coach.html', {'form': form})