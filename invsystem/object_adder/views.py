from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def add(request):
    context = {'title': 'Objekt inventarisieren'}

    return render(request, 'object_adder/index.html', context)
