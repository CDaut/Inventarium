from django.shortcuts import render, get_object_or_404
from object_adder.models import Object, Category
from object_adder.forms import ObjectForm
from django.contrib.auth.decorators import login_required
import re


# Create your views here.
@login_required
def objlist(request, orderstr=None):
    uuidv4pattern = r"(\d|[a-z]){8}-(\d|[a-z]){4}-4(\d|[a-z]){3}-(\d|[a-z]){4}-(\d|[a-z]){12}"

    if request.method == 'GET':

        if orderstr is None:
            objects = Object.objects.all()
        elif orderstr == '0':
            objects = Object.objects.all().order_by('title')
        elif orderstr == '1':
            objects = Object.objects.all().order_by('ammout')
        elif orderstr == '2':
            objects = Object.objects.all().order_by('category')
        elif orderstr == '3':
            objects = Object.objects.all().order_by('inventarized_date')
        elif orderstr == '4':
            objects = Object.objects.all().order_by('user_added')
        else:
            result = re.fullmatch(uuidv4pattern, orderstr)
            if result is None:
                objects = Object.objects.all()
            else:
                uuid = result.group(0)
                obj = get_object_or_404(Object, pk=uuid)

                form = ObjectForm(
                    initial={'ammout': obj.ammout, 'title': obj.title, 'description': obj.description,
                             'category': obj.category}
                )

                context = {'title': 'Details', 'obj': obj, 'form': form}

                return render(request, 'object_lister/details.html', context)

        categories = Category.categories.all()

        context = {'title': 'Inventar', 'objects': objects, 'objammout': len(objects), 'categories': categories,
                   'ncats': len(categories)}
        return render(request, 'object_lister/index.html', context)

    elif request.method == 'POST':
        form = ObjectForm(request.POST, request.FILES)

        if form.is_valid():
            result = re.fullmatch(uuidv4pattern, orderstr)

            uuid = result.group(0)
            obj = get_object_or_404(Object, pk=uuid)

            obj.ammout = form.cleaned_data['ammout']
            obj.title = form.cleaned_data['title']
            obj.description = form.cleaned_data['description']
            obj.category = form.cleaned_data['category']

            obj.save()

            form = ObjectForm(
                initial={'ammout': obj.ammout, 'title': obj.title, 'description': obj.description,
                         'category': obj.category}
            )

            context = {'title': 'Details', 'obj': obj, 'form': form, 'message': 'changed'}

            return render(request, 'object_lister/details.html', context)


@login_required
def delete(request, uuid_url):
    obj = get_object_or_404(Object, pk=uuid_url)
    obj.delete()
    return render(request, 'object_lister/delete.html', {'uuid': uuid_url})


@login_required
def deleteCategory(request, uuid_url):
    cat = get_object_or_404(Category, pk=uuid_url)
    cat.delete()
    return render(request, 'object_lister/delete.html', {'uuid': uuid_url})
