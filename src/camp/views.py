# camps/views.py
from django.shortcuts import render, redirect
from .models import Camp
from .forms import CampRegistrationForm

def index(request):
    all_camps = Camp.objects.order_by('start_date')
    context = {'camps': all_camps}
    return render(request, 'camps/index.html', context)

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