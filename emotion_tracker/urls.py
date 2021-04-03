from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "emotion_tracker"
urlpatterns = [
    path('', views.emotion_tracker, name='emotion_tracker'),
    path('details/<pk>', views.emotion_detail, name='emotion_detail'),
    path('update/<pk>', views.update_emotion, name='emotion_update'),
    path('delete/<pk>', views.delete_emotion, name='emotion_delete'),



   
]
