from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms
from django import forms
from .models import Sleep
from datetime import datetime
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime
from bootstrap_datepicker_plus import DateTimePickerInput,DatePickerInput
class AddSleepForm(forms.ModelForm):
    class Meta:
        model = Sleep
        fields = '__all__'
        exclude = ['user']
        widgets = {
             "start": DateTimePickerInput(options= {'maxDate': 'now' }),
            "end": DateTimePickerInput(options= {'maxDate': 'now' }),
        }
       

      