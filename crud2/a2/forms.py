from django.forms import ModelForm
from django import forms
from .models import Table,Video

class TestForm(ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        # widgets = {'name': forms.TextInput(attrs = {'class':"form-control",
        #                                             'placeholder':"Ad"})}

class videoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
