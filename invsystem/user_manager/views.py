from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import SignUpForm


def index(request):
    return render(request, 'user_manager/index.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        title = 'Login'

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = SignUpForm()
        title = 'Registrieren'

    context = {'form': form, 'title': title}
    return render(request, 'registration/register.html', context)
