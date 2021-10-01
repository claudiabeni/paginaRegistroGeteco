from django import forms
from django.forms import fields
from django.forms.fields import Field
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields ='__all__'