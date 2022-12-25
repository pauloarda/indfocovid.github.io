from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2","first_name","last_name", "email")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        # user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user