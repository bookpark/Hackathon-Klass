from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from .forms import SignupForm, SigninForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('member:login')
    else:
        form = SignupForm
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.login(request)
        return redirect('member:login')
    else:
        form = SigninForm
    context = {
        "form": form,
    }
    return render(request, 'member/signin.html', context)


def signout(request):
    logout(request)
    return redirect('member:login')
