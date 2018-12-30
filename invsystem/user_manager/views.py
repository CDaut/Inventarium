from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

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


@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            log = open(settings.LOGFILE, 'a')
            log.write(
                '\n[' + str(timezone.now()) + ']' + ' CHANGE_PWD: |USR: ' + request.user.username
            )

            form = PasswordChangeForm(request.user)
            context = {'title': 'Passwort ändern', 'form': form, 'message': 'PWD_CHANGE_SUCCESS'}
            return render(request, 'registration/changepwd.html', context)
        else:
            form = PasswordChangeForm(request.user)
            context = {'title': 'Passwort ändern', 'form': form, 'message': 'PWD_CHANGE_FALURE'}
            return render(request, 'registration/changepwd.html', context)

    else:
        form = PasswordChangeForm(request.user)
        context = {'title': 'Passwort ändern', 'form': form}
        return render(request, 'registration/changepwd.html', context)
