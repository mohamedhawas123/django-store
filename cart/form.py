from django import forms
from .models import AddressUser



class AddrssUser(forms.ModelForm):

    
    class Meta:
        model = AddressUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address_line', 'city', 'state', 'country', 'order_note']


    
