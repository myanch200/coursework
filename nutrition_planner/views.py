from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe,Nutrition
@login_required(login_url='accounts:login')
def nutrition_planner(request):
    recipes = Recipe.objects.all()
    
    context = {'recipes':recipes}
    return render(request,'nutrition_planner/nutrition-planner.html',context)

@login_required(login_url='accounts:login')
def detailed_recipe(request,pk):
    recipe = Recipe.objects.get(id = pk)
    nutritions = Nutrition.objects.filter(recipe= recipe.id)
    context = {'recipe': recipe,'nutritions':nutritions}
    return render(request,'nutrition_planner/detailed_recipe.html',context)
