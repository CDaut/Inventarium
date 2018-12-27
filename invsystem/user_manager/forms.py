from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = CharField(required=True)
    last_name = CharField(required=True)
    first_name = CharField(required=True)
    email = CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
