from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.product.models import *


@login_required
def index(request):
    products = Products.objects.filter(user=request.user)
    product_category = ProductCategory.objects.filter()
    context = {
        'products': products,
        'product_category': product_category,
    }
    return render(request, "index.html", context)


def notFound(request):
    return render(request, "404.html", {})
