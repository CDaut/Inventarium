from django.forms import ModelForm, TextInput

from .models import Object


class ObjectForm(ModelForm):
    class Meta:
        model = Object
        fields = ('ammout', 'title', 'img', 'description')
        widgets = {
            'title': TextInput(),
        }
