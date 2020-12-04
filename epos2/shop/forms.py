from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    firstName = forms.CharField(max_length=100, required = True)
    lastName = forms.CharField(max_length=100, required = True)
    email = forms.EmailField(max_length=254, help_text = 'eg. example@test.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')