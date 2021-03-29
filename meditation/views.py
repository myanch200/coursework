from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import YogaArticle
@login_required(login_url='accounts:login')
def meditation(request):
    return render(request,'meditation/meditation.html')


def yoga_main(request):
    yoga_articles = YogaArticle.objects.all()
    context = {'articles':yoga_articles}
    return render(request,'meditation/yoga_main.html',context)