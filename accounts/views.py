from django.shortcuts import render, redirect
from .form import FormRegisteration
from .models import Account
from django.contrib import messages, auth
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password, check_password
from cart.models import AddressUser
from cart.models import CartItem


def login(request):
    
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            
            return redirect('home')
        else:
            messages.error(request, 'something went wrong')
            return redirect('login')

    
    return render(request, 'accounts/login.html')




def register(request):
    if request.method == 'POST':
        form = FormRegisteration(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0] 
            user = Account.objects.create_user(
                first_name=first_name,
                email=email,
                last_name=last_name,
                password=password,
                username=username
            )
            user.phone_number = phone_number
            user.save()

            current_site = get_current_site(request)
            mail_subject = "please activate your account"

            message = render_to_string('accounts/account_veri_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)

            })
            print(message)

            to_email = email

            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'register done')
            return redirect('login')
        else:
            form= FormRegisteration()


    form = FormRegisteration()
    return render(request, 'accounts/register.html', {'form': form}) 


def logout(request):

    user = auth.logout(request)
    return redirect('home')



def activate(request, uidb64, token):

    # try:
    #     uid=  urlsafe_base64_decode(uidb64).decode()
    #     user= Account._default_manager.get(pk=uid)
    
    # except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
    #     user = None
    
    # if user is not None and default_token_generator.check_token(token):
    #     user.is_active = True
    #     user.save()
    #     messages.success(request, 'congrats')
    #     return redirect('login')
    
    # else:

    #     messages.error(request, 'something went wrong')
    #     return redirect('register')



    return
    
    

def dash(request):
    accountt =AddressUser.objects.get(user=request.user)
    print(accountt.address_line)
    
    cart = CartItem.objects.filter(user=request.user)
    
    return render(request, 'accounts/dash.html', {'pro': accountt, 'cart': cart})


def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get("password")
        user = Account.objects.get(email=email)
        print(user)
        old_password= request.POST.get("old_password")
        if user.check_password(old_password):
            
            user.password = make_password(password)
            user.save()
        else:
            print("false")

        
        print("i got here")
    return render(request, 'accounts/forget.html')