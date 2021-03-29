from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def meditation(request):
    return render(request,'meditation/meditation.html')