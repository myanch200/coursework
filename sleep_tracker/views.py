from django.shortcuts import render
from .forms import AddSleepForm
# Create your views here.
def sleep_tracker(request):
    form = AddSleepForm()
    context = {'form': form}
    return render(request,'sleep_tracker/dashboard.html',context)