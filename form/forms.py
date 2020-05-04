from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class EntryForm(forms.ModelForm):

    class Meta:
        model = entry
        fields = '__all__'
