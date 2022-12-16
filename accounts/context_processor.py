from django.contrib import auth




def menu_linkes(request):
    user= auth.get_user(request)

    print(user)
    return dict(user=user)