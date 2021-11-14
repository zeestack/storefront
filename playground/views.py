from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# request -> response
# action

def say_hello(request):
    # return HttpResponse("Hello World")
    return render(request, 'hello.html', {"name" : "Zahid Hussain", "age" : 37})

