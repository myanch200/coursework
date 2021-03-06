from django.shortcuts import render
from .models import Exercise
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def exercise(request):
    exercises = Exercise.objects.all()
    context = {'exercises':exercises}
    return render(request, 'exercises/exercises.html',context)


def exercise_detail(request,pk):
    exercise = Exercise.objects.get(id=pk)
    return render(request, 'exercises/exercise_detail.html',{'exercise': exercise})