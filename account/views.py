from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from . import forms, models


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('PalePink:home'))
        else:
            return render(request, 'common/home.html', {'username': username, 'password': password})
    if request.method == 'GET':
        return render(request, 'common/home.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('PalePink:home'))


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('account:login'))
        else:
            return HttpResponse('fail')
    else:
        form = forms.RegisterForm()
        return render(request, 'account/register.html', {"form": form})


def background(request):
    return render(request, 'account/user_profile.html')

