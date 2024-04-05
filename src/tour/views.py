from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import TourQuoteForm

def index(request):
    context = {}
    return render(request, 'tour/index.html', context)

def tour_quote(request):
    if request.method == 'POST':
        form = TourQuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your tour quote request has been submitted successfully!")
            return redirect('success_page')
    else:
        form = TourQuoteForm()
    return render(request, 'tour/tour_quote.html', {'form': form})