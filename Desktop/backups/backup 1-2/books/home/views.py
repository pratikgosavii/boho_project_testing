from django.shortcuts import render
from cart.models import cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import books

# Create your views here.






def index(request):

    subtotal = 0
    if request.user.is_authenticated:

        dests_usercart = cart.objects.filter(buyer=request.user)


       
        for dest in dests_usercart:
            subtotal = subtotal + int(dest.product_id.price)

        
    else:
        dests_usercart = None


    
        
    #categories on homescreen view

    dests_categoryall = books.objects.all()
    dests_categorybiographic = books.objects.filter(category = 'biographic')
    dests_categoryadventure = books.objects.filter(category = 'adventure')
    dests_categorykids = books.objects.filter(category = 'kids')
    dests_categorycook = books.objects.filter(category = 'cook')
    dest_relevant = books.objects.order_by("?")

    if request.user.is_authenticated:
        cart_count = cart.objects.filter(buyer = request.user).count()
    else:
        cart_count = None

    dests_categoryall_count = dests_categoryall.count()
    dests_categorybiographic_count = dests_categorybiographic.count()
    dests_categoryadventure_count = dests_categoryadventure.count()
    dests_categorykids_count = dests_categorykids.count()
    dests_categorycook_count = dests_categorycook.count()
    dest_relevant_count = dest_relevant.count()



    #popular on homescreen view
    dests_popular = books.objects.filter(popular = True)


    context= {
        
        'cart_count' : cart_count,
        'dests_categoryall_count' : dests_categoryall_count,
        'dests_usercart' : dests_usercart,
        'totalprice' : subtotal,
        'dests_categoryall' :  dests_categoryall,
        'dests_categorybiographic' : dests_categorybiographic,
        'dests_categoryadventure' : dests_categoryadventure,
        'dests_categorykids' : dests_categorykids,
        'dests_categorycook' : dests_categorycook,
        'dests_popular' :  dests_popular,
        'dest_relevant' : dest_relevant
        
    }

    return render(request, 'index.html', context)


    



def about(request):

    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')


def asa(request):

    return render(request, 'about.html')

