from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product


# Create your views here.

# request -> response
# action


def say_hello(request):
    # return HttpResponse("Hello World")
    # query_set = Product.objects.all() # query_set is based on lazy evaluation
    # for product in query_set:
    #  print(product)
    # try:
    #   product = Product.objects.get(pk=1)
    # except ObjectDoesNotExist:
    #   pass
    exists = Product.objects.filter(pk=1).exists()
    product = Product.objects.filter(pk=1).first()
    print(product)
    return render(request, "hello.html", {"name": "Zahid Hussain", "age": "37"})
