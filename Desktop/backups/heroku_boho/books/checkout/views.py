from django.shortcuts import render,  HttpResponseRedirect, reverse

# Create your views here.

from cart.models import cart
import math
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from .forms import *
from home.models import books


# Create your views here.


def checkout(request):

    if request.user.is_authenticated:
        dests = cart.objects.filter(buyer = request.user)

        cart_count = 0
        cart_count = cart.objects.filter(buyer = request.user).count()

        cart_total = 0

        for dest in dests:

            cart_total = cart_total + int(dest.product_id.price)
        print('cart total')
        print(cart_total)

        if request.session.get('coupon_applied', None) != None:

            coupon_name = request.session.get('coupon_name')
            discount_amount = request.session.get('discount_amount')
            coupon_applied = request.session.get('coupon_applied')
            discount_amount = math.ceil(discount_amount)
            cart_total_afterdiscount = cart_total - discount_amount
        
        else: 
            cart_total_afterdiscount = cart_total
            discount_amount = None
            coupon_name = None
            coupon_applied = None

        
        context= {

            'dests' : dests,
            'cart_count' : cart_count,
            'cart_total' : cart_total,
            'discount_amount' : discount_amount,
            'cart_total_afterdiscount' : cart_total_afterdiscount,
            'coupon_name' : coupon_name,
            'coupon_applied' : coupon_applied
            }

        return render(request, 'checkout.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))



def order_place(request):

    if request.user.is_authenticated:

        if request.method == 'POST':

            form=orderplace_detail_form(request.POST)
            form2=orderplace_detail_form(request.POST)
            print(form.errors)
           
            if form.is_valid():

                instance = form.save(commit=False)
              

                books_count = cart.objects.filter(buyer = request.user).count()
                books_array = cart.objects.filter(buyer = request.user).count()
                
                for x in range(books_count):

                    placedorder_book = books_array[x]
                    buyer = request.user

                    # i have to creata 2 form


                instance.save()
                
                return HttpResponseRedirect(reverse('index'))
                
            else:
                
                return HttpResponseRedirect(reverse('checkout'))

        else:
            print('somethong went wrong')
            return render(request, 'contact.html')

    else:
        print('login first')

        return render(request, 'loginsignup.html')



