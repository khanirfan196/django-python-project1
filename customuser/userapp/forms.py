from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Please enter valid email!')

    class Meta:
        model = Account
        fields = ("email","username","password1","password2")


