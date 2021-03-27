from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import AddSleepForm
from .models import Sleep
# Create your views here.
def sleep_tracker(request):
    form = AddSleepForm(instance = request.user)
    if request.method == 'POST':
        form = AddSleepForm(request.POST,instance = request.user)
        if form.is_valid():
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')
            sleep = Sleep(user= request.user, start=start, end=end)
            sleep.save()
            return(redirect("sleep_tracker:dashboard"))
        else:
            messages.error(request,"Please fill all the fields")
    
    sleep_data = Sleep.objects.filter(user=request.user.id).order_by('end')[:5]

    context = {'form': form,'sleep_data': sleep_data}
    return render(request,'sleep_tracker/dashboard.html',context)