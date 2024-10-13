from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


"""
This form is a custom user registration form that collects a username,
email, password.

Ensures email is required and saves the new user in the database

The 'save' method is customized to handle setting the email field before saving the user
"""
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

