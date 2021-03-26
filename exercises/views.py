from django.shortcuts import render
from .models import Exercise
# Create your views here.
def exercise(request):
    
    
    return render(request, 'exercises/exercises.html')