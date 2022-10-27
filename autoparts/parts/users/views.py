from django.shortcuts import render, redirect
from django.contrib import auth, messages
from autoparts.models import Journal
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from autoparts.models import Car


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required(login_url='/users/login')
def profile(request):
    car=Car.objects.all()
    user = request.user
    if request.method == "POST":
        user.car_name=request.POST['length']
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    journal = Journal.objects.all()


    context = {
        'form': form,
        'journal':journal,
        'car':car,
    }
    return render(request, 'users/profile.html', context)

@login_required(login_url='/users/login')
def logout(request):
    auth.logout(request)
    return redirect('index')

