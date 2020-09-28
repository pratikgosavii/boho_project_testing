from django.shortcuts import render,  HttpResponseRedirect, reverse

# Create your views here.

from cart.models import cart
import math
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
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

        if request.session.get('discount_amount', None) != None:

            coupon_name = request.session.get('coupon_name')
            discount_amount = request.session['discount_amount']
            discount_amount = math.ceil(discount_amount)
            cart_total_afterdiscount = cart_total - discount_amount
        
        else: 
            discount_amount = 00

        
        context= {

            'dests' : dests,
            'cart_count' : cart_count,
            'cart_total' : cart_total,
            'discount_amount' : discount_amount,
            'cart_total_afterdiscount' : cart_total_afterdiscount,
            'coupon_name' : coupon_name
            }

        return render(request, 'checkout.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))



