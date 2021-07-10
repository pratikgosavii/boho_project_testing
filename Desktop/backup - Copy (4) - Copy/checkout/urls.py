from django.urls import path, include

from . import views


urlpatterns=[

path('', views.checkout_page, name='checkout'),   
path('checkout_singleproduct/<booki>', views.checkout_single_page, name='checkout_single'),
path('address', views.checkout_address, name='checkout_address'),   
path('address_session', views.address_session, name='address_session'),   
path('payment', views.payment, name='payment'),   
path('place_order', views.place_order_laptop, name='place_order_laptop'),   

path('coupon_session_close', views.coupon_session_close, name='coupon_session_close'),   

path('mobile_address', views.mobile_address, name='mobile_address'),
path('mobile_add_address', views.mobile_add_address, name='mobile_add_address'),
path('mobile_order_summary', views.mobile_order_summary, name='mobile_order_summary'),
path('mobile_payment', views.mobile_payment, name='mobile_payment'),

path('placeorder', views.place_order, name='place_order'),
path('mobile_placeorder', views.mobile_placeorder, name='mobile_placeorder'),
path('edit_saved_address', views.edit_address, name='edit_address'),
]