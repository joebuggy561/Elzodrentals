from django.shortcuts import render
from .models import Products


def home(request):
    products = Products.objects.all().filter()

    context = {
        'products' : products
    }
    return render(request, "home.html", context)

# Create your views here.
