from django.shortcuts import render
from .form import FormRegisteration


def login(request):
    
    return render(request, 'accounts/login.html')




def register(request):
    form = FormRegisteration()
    return render(request, 'accounts/register.html', {'form': form}) 


def logout(request):
    pass

