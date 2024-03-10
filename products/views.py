from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product':product})
    # return HttpResponse("<h1>welcome to django</h1>")
def about(request):
    return HttpResponse("<h1>about page</h1>")
def contact(request):
    return HttpResponse("<h1>contact details</h1>")
def offer(request):
    return HttpResponse("<h1>offer applied</h2>")