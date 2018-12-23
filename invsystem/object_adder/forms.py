from django.forms import ModelForm, TextInput

from .models import Object, Category


class ObjectForm(ModelForm):
    class Meta:
        model = Object
        fields = ('ammout', 'title', 'img', 'description', 'category')
        widgets = {
            'title': TextInput(),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': TextInput()
        }
