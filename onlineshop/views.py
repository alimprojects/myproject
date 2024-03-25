from http.client import HTTPResponse
from itertools import product
from urllib import request
from django.shortcuts import render, redirect

from .models import *
from .forms import ContactForm, ReviewForm

# Create your views here.
def landing(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()
    return render(request, "index.html", context)

def product(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(ProductID=id)
    context["rev"] = Review.objects.filter(product_id=id) 
         
    return render(request, "product.html", context)

def contact(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('contact')
    return render(request, "contact.html")

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.save()
            id = request.POST.get('ProductID')
            return redirect('product', id = id) 
        else:
            return  HTTPResponse("Form is not valid")
    else:
        return HTTPResponse ("method not allowed", status=400)
