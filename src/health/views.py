from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
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

def download_plan_file(request, plan_id):
    health_plan = get_object_or_404(HealthPlan, pk=plan_id)
    file_path = health_plan.file.path
    
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{health_plan.file.name}"'
        return response
