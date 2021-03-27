from django.shortcuts import render
from .models import Exercise
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def exercise(request):
    
    
    return render(request, 'exercises/exercises.html')