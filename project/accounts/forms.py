from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}), label='Email')


class CustomUserCreationForm(UserCreationForm):
    username = forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
        }
