from django import forms
from django.core import validators

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
