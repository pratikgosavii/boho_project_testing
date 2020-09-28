from django import forms
from .models import *


class orderplace_detail_form(forms.ModelForm):
    
    name =                  forms.CharField(widget=forms.TextInput())
    mobilenumber =          forms.IntegerField() 
    pincode =               forms.IntegerField() 
    address_full =          forms.CharField(widget=forms.TextInput())
    landmark =              forms.CharField(widget=forms.TextInput())
   
    
    class Meta():
        model = placeorder_detail
        fields = ['name', 'mobilenumber', 'pincode', 'address_full', 'landmark']




    
    


