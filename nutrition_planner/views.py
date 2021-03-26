from django.shortcuts import render

# Create your views here.
def nutrition_planner(request):
    return render(request,'nutrition_planner/nutrition-planner.html',{})