from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HealthPlan
from .forms import FitnessEvaluationForm

def index(request):
    health_plans = HealthPlan.objects.all()
    context = {
        'health_plans': health_plans,
    }
    return render(request, 'health/index.html', context)

def submit_fitness_evaluation(request):
    if request.method == 'POST':
        form = FitnessEvaluationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your fitness evaluation has been submitted successfully!")
            return redirect('success_page')
    else:
        form = FitnessEvaluationForm()
    return render(request, 'health/submit_fitness_evaluation.html', {'form': form})
