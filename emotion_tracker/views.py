from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .forms import DiaryForm
from .models import Diary
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='accounts:login')
def emotion_tracker(request):
    diary_results = Diary.objects.filter(user=request.user )
    form = DiaryForm(instance=request.user)
    if request.method == 'POST':
        form = DiaryForm(request.POST,instance=request.user)
        if form.is_valid():
            emotion = form.cleaned_data.get('emotion')
            comment = form.cleaned_data.get('comment')
            diary = Diary(user=request.user,emotion=emotion,comment=comment)
            diary.save()
            
    context = {
       'form': form,'results':diary_results
    }
    return render(request,'emotion_tracker/emotion-tracker.html',context)

def update_emotion(request,pk):
    emotion_entry = Diary.objects.get(id=pk)
    form = DiaryForm(instance=emotion_entry)
    if request.method == 'POST':
        form = DiaryForm(request.POST,instance=emotion_entry)
        if form.is_valid():
            form.save()
            return redirect('emotion_tracker:emotion_tracker')
    context = {
        'form': form,
    }
    return render(request,'emotion_tracker/emotion_update.html',context)

def emotion_detail(request,pk):
    diary_results = Diary.objects.filter(user=request.user)
    diary_entry = diary_results.get(id=pk)
    
    
   
    return render(request,'emotion_tracker/emotion_details.html',{'result':diary_entry})
def delete_emotion(request,pk):
    emotions_entry = Diary.objects.filter(user=request.user)
    emotion = emotions_entry.get(id=pk)
    emotion.delete()
    return redirect('emotion_tracker:emotion_tracker')
