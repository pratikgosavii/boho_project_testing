from django.urls import path, include

from . import views


urlpatterns=[

path('', views.index, name='index'),
path('contact', views.contact, name='contact'),
path('about', views.about, name='about'),
path('aa/', views.asa, name='addorg'),

#all imports here

path('', include('study_books.urls')),

]