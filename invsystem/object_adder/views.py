from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from os.path import join
from .forms import ObjectForm, CategoryForm
from django.utils import timezone


# Create your views here.

@login_required
def add(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                obj = form.save(commit=True)
            except OverflowError:
                context = {'title': 'Fehler!',
                           'error': 'Weder in den Chemieraum noch in eine Variable des Datentypes SQLite INTEGER passen mehr als 9223372036854775807 Objekte. Bitte inventarisieren sie das Objekt neu.'}
                return render(request, 'object_adder/error.html', context)

            obj.inventarized_date = timezone.now()
            obj.removed_date = None
            obj.user_added = request.user
            obj.save()

            log = open(settings.LOGFILE, 'a')
            log.write(
                '\n[' + str(timezone.now()) + ']' + ' CREATE_OBJECT ' + '|USR: ' + request.user.username + '|NAME: ' +
                form.cleaned_data['title'] + '|UUID: ' + str(obj.uuid) + '|CAT: ' + str(obj.category)
            )

            context = {'title': 'Objekt inventarisieren', 'form': ObjectForm,
                       'obj_name': form.cleaned_data.get('title')}
            return render(request, 'object_adder/index.html', context)

    else:
        context = {'title': 'Objekt inventarisieren', 'form': ObjectForm}
        return render(request, 'object_adder/index.html', context)


@login_required
def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat = form.save()
            cat.save()

            log = open(settings.LOGFILE, 'a')
            log.write(
                '\n[' + str(timezone.now()) + ']' + ' CREATE_CATEGORY ' + '|USR: ' + request.user.username + '|NAME: ' +
                cat.name + '|UUID: ' + str(cat.id)
            )

            context = {'title': 'Neue Kategorie hinzufügen',
                       'cat_name': form.cleaned_data.get('name'),
                       'form': CategoryForm}
            return render(request, 'object_adder/category.html', context)
    else:
        context = {'form': CategoryForm, 'title': 'Neue Kategorie hinzufügen'}
        return render(request, 'object_adder/category.html', context)
