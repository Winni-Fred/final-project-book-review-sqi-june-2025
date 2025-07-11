from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=200, required=True)
    terms = forms.BooleanField(required=True)
    newsletter = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

