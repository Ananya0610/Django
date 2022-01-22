from django import forms
from django.core import validators

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    vmail=forms.EmailField(label="ENTER AGAIN!")
    text=forms.CharField(widget=forms.Textarea)


    def clean(self):
        all_cleaned_data=super().clean()
        email=all_cleaned_data['email']
        vmail=all_cleaned_data['vmail']

        if email!=vmail:
            raise forms.ValidationError("make sure emails match")
