from django.shortcuts import render

# Create your views here.
def emotion_tracker(request):
    return render(request,'emotion_tracker/emotion-tracker.html')