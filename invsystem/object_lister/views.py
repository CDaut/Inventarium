from django.shortcuts import render
from object_adder.models import Object
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def objlist(request):

    objects = Object.objects.all()

    context = {'title': 'Inventar', 'objects': objects}
    return render(request, 'object_lister/index.html', context)
