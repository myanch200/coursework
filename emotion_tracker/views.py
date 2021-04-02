from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .forms import DiaryForm
from .models import Diary

@login_required(login_url='accounts:login')
def emotion_tracker(request):
    form = DiaryForm(instance=request.user)
    if request.method == 'POST':
        form = DiaryForm(request.POST,instance=request.user)
        if form.is_valid():
            emotion = form.cleaned_data.get('emotion')
            comment = form.cleaned_data.get('comment')
            diary = Diary(user=request.user,emotion=emotion,comment=comment)
            diary.save()
            return redirect('accounts:home')
    context = {
       'form': form,
    }
    return render(request,'emotion_tracker/emotion-tracker.html',context)