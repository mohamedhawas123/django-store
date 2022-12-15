from django import forms
from .models import Account



class FormRegisteration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholer': 'enter password',
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        ' enter repeated password '
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']