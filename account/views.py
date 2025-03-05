from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import  login, logout

from account.forms import LoginForm, UserEditForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:main')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            login(request, user)
            return redirect('home:main')

    return render(request,'account/login.html', {'form':form})


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


def user_edit(request):
    if not request.user.is_authenticated:
        return redirect('account:login')
    user = request.user
    form = UserEditForm(instance=user)
    if request.method =='POST':
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'account/edit_info.html',{'form':form})
def user_logout(request):
    logout(request)
    return redirect('home:main')