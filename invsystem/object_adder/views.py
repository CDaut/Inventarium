from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ObjectForm
from django.utils import timezone


# Create your views here.

@login_required
def add(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST)

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

        context = {'title': 'Objekt inventarisieren', 'form': ObjectForm,
                   'obj_name': form.cleaned_data.get('title')}
        return render(request, 'object_adder/index.html', context)

    else:
        context = {'title': 'Objekt inventarisieren', 'form': ObjectForm}
        return render(request, 'object_adder/index.html', context)
