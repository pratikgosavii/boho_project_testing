from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
       

        user = auth.authenticate(username = email, password = password)

        if user is not None:
            auth.login(request, user)

            return HttpResponseRedirect(reverse('index'))

        else:
            messages.error(request, ' invalid creddentils')
            return render(request, 'loginsignup.html')

    else:
        messages.warning(request, 'Somethings went wrong, contact us')
        return render(request, 'loginsignup.html')



def loginsignuphome(request):
    return render(request, 'loginsignup.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        




        if password1 == password2 :

            if User.objects.filter(email = email).exists():
                messages.warning(request, 'Email exists ! Try to login ')
                return render(request, 'loginsignup.html')
           

            else:
                user = User.objects.create_user(  username = email, password = password1 )
                user.save()
                messages.success(request, 'register successful, login to start new trip with us !')
                return render(request, 'loginsignup.html')


        else:

            messages.warning(request, 'password does not match')
            return render(request, 'loginsignup.html')

    else:
        messages.warning(request, 'something went wrong, contact us')
        return render(request, 'loginsignup.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You are now logout')
    return redirect('/')

