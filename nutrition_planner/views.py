from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def nutrition_planner(request):
    return render(request,'nutrition_planner/nutrition-planner.html',{})