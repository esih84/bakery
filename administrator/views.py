from django.shortcuts import render

from administrator.models import post


# Create your views here.

def landing(requests):
    context={
        "post": post.objects.all()
    }
    return render(requests, "administrator/product.html", context)
