from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import RegisterUserForm
# Create your views here.
def home(request):
    return render(request,'accounts/index.html',{})


def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    context = {
        'form': form,
    }
    return render(request,'accounts/register.html',context)

def user_login(request):
    
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password =password)
            if user is not None:
                login(request, user)
                messages.success(request,f'{user.username} successfully logged in')
                return redirect('/')

            else:
                messages.error(request,"Wrong username or password")
    context = {'form':form}
       
    return render(request,'accounts/login.html',context)


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('accounts:home')