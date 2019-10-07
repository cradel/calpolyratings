from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import MyLoginForm
from allauth.account.views import SignupView, LoginView

from .validators import username_checker


# ajax view for red or green username label at registration
def check_username(request):
    username = request.GET.get('username')

    if User.objects.filter(username=request.GET.get('username')).exists():
        return HttpResponse('red', content_type='text/plain')

    # now run the username through validator
    try:
        username_checker(username)
        return HttpResponse('green', content_type='text/plain')
    except:
        return HttpResponse('red', content_type='text/plain')
