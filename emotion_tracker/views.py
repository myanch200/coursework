from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def emotion_tracker(request):
    return render(request,'emotion_tracker/emotion-tracker.html')