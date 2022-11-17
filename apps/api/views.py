import hashlib

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render

from apps.product.models import *


def login_control(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    user_cont = User.objects.get(email=email)
    if not user_cont.check_password(password):
        data = "Başarılı"
        login(request, user_cont, backend='django.contrib.auth.backends.ModelBackend')
    else:
        data = "Başarısız"
    context = {
        'data': data,
    }
    return render(request, "apps/api/data.html", context)


def login_control_login(request):
    if request.user:
        email = request.user.email
        password = request.user.password
        statu = "Başarılı"
        data = str(statu) + "{//}" + str(email) + "{//}" + str(password)
    else:
        statu = "Başarısız"
        data = str(statu)
    context = {
        'data': data,
    }
    return render(request, "apps/api/data.html", context)


def mainPageApi(request):
    products = Products.objects.filter()
    product_category = ProductCategory.objects.filter()
    context = {
        'products': products,
        'product_category': product_category,
    }
    return render(request, "apps/api/index_api.html", context)
