from django.shortcuts import render,  HttpResponseRedirect, reverse

# Create your views here.

from cart.models import cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from home.models import books

# Create your views here.


def checkout(request):

    if request.user.is_authenticated:
        dests = cart.objects.filter(buyer = request.user)

        cart_total = 0

        for dest in dests:

            cart_total = cart_total + int(dest.product_id.price)

        context= {

                'dests' : dests,
                'cart_total' : cart_total,
            }

        return render(request, 'checkout.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))



