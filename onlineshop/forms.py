from dataclasses import fields
from django import forms
from .models import *

class ContactForm(forms.ModelForm):    
    class Meta:
        model = Contact       
        fields = ["Name", "Email", "Massage"]
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  
        fields = ["product_id", "Name", "Email", "Review", ]  
        exlude = ['date']