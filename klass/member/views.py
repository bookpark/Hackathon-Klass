from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('member:login')
    else:
        form = SignupForm
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
        return redirect('member:login')
    else:
        form = LoginForm
    context = {
        "form": form,
    }
    return render(request, 'member/login.html', context)
