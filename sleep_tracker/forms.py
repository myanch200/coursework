from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Sleep
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime
class AddSleepForm(ModelForm):
    class Meta:
        model = Sleep
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'start': AdminSplitDateTime(),
            'end': AdminSplitDateTime(),
        }