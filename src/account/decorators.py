from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

def manager_required(view_func):
    """
    Decorator for views that checks if the user is in the 'Manager' group.
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to dashboard function
            return redirect('accounts:dashboard')
    return _wrapped_view