from django.shortcuts import render
from django.contrib import messages

from .forms import AddSleepForm
from .models import Sleep
# Create your views here.
def sleep_tracker(request):
    form = AddSleepForm(instance = request.user)
    if request.method == 'POST':
        form = AddSleepForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
        else:
            messages.error(request,"Please fill all the fields")
    
    sleep_data = Sleep.objects.all()
    context = {'form': form,'sleep_data': sleep_data}
    return render(request,'sleep_tracker/dashboard.html',context)