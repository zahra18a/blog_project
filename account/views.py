from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:main')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:main')
    return render(request,'account/login.html', context={})


def user_register(request):
    context = {"errors": []}
    if request.user.is_authenticated:
        return redirect('home:main  ')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password != re_password:
            context['errors'].append('passwords do not match')
            return  render(request,'account/register.html', context = context)
        # if User.objects.get(username=username):
        #     context['errors'].append('this username is exists')
        #     return  render(request,'account/register.html', context = context)
        email = request.POST.get('email')
        user = User.objects.create(username=username, email=email, password=password)
        login(request, user)
        return redirect('home:main')
    return render(request, 'account/register.html', context={})

def user_logout(request):
    logout(request)
    return redirect('home:main')