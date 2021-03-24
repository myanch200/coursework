from django.shortcuts import render
from .models import Exercise
# Create your views here.
def exercise(request,pk):
    exercises = Exercise.objects.get(pk=pk)
    context = {'exercise': exercises}
    return render(request, 'exercises/exercise.html', context)