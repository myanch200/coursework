from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe,Nutrition
@login_required(login_url='accounts:login')
def nutrition_planner(request):
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
    return render(request,'nutrition_planner/nutrition-planner.html',context)