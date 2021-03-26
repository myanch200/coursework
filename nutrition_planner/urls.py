from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "nutrition_planner"
urlpatterns = [
    path('', views.nutrition_planner, name='nutrition_planner'),
   
]
