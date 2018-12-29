from django.forms import CharField,Form
from django.contrib.auth.models import User


class SettingsForm(Form):
    username = CharField(required=False)
    last_name = CharField(required=True)
    first_name = CharField(required=True)
    email = CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
