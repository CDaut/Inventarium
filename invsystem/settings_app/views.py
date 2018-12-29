from django.shortcuts import render
from .forms import SettingsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


@login_required
def index(request):
    if request.method == 'GET':
        user = request.user
        default = {'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name,
                   'email': user.email}
        form = SettingsForm(initial=default)
        context = {'title': 'Einstellungen', 'form': form}
        return render(request, 'settings_app/settings.html', context)

    elif request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        form = SettingsForm(request.POST)

        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()

            default = {'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name,
                       'email': user.email}
            form = SettingsForm(initial=default)
            context = {'title': 'Einstellungen', 'form': form, 'edited': True}
            return render(request, 'settings_app/settings.html', context)

        else:
            default = {'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name,
                       'email': user.email}
            form = SettingsForm(initial=default)
            context = {'title': 'Einstellungen', 'form': form}
            return render(request, 'settings_app/settings.html', context)
