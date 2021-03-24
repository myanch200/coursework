from django.shortcuts import render

# Create your views here.
def sleep_tracker(request):
    return render(request,'sleep_tracker/dashboard.html',{})