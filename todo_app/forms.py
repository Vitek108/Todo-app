from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from todo_app.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["name", "description", "comment", "status", "due_date"]


class TodoForm2(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["comment", "status"]


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']