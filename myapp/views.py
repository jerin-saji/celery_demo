from django.shortcuts import render
from celerydemo.celery import add

# Create your views here.

def index(request):
    print("Results: ")
    result1 = add.delay(10, 20)
    print("Result 1: ", result1)
    print("ready :",result1.ready())
    # print("Successful:", result1.successful())

    return render(request, "myapp/home.html")


def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')