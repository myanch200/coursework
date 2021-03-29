from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "emotion_tracker"
urlpatterns = [
    path('', views.emotion_tracker, name='emotion_tracker'),
   
]
