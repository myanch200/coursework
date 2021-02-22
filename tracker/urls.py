
from django.urls import path
from .views import dashboard

app_name = "tracker"
urlpatterns = [
    path('', dashboard, name='dashboard')
]
