from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


class BayForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput)
    street = forms.CharField(widget=forms.TextInput)
    house = forms.CharField(widget=forms.TextInput)
    apartment = forms.CharField(widget=forms.TextInput)
    delivery = forms.CharField(widget=forms.CheckboxInput)


class UserCreationForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        exclude = ('date_subscribed', 'messages_received')
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)
