from django.forms import forms, ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EntryForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
