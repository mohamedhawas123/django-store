from django import forms
from .models import Account



class FormRegisteration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholer': 'enter password',
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'enter repeated password '
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    

    def __init__(self, *args,  **kwargs):
        super(FormRegisteration, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'enter your last name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'enter your Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'enter your Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



    def clean(self):
        clean_data = super(FormRegisteration, self).clean()
        passwrd = clean_data.get('password')
        confirem_password =clean_data.get('confirm_password')

        if passwrd != confirem_password:
            raise forms.ValidationError(
                "Password does not match"
            )