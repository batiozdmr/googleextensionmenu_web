from django.urls import path

from .views import *

app_name = "api"

urlpatterns = [
    path('login_control/', login_control, name='login_control'),
    path('login_control_login/', login_control_login, name='login_control_login'),
    path('productData/', productData, name='productData'),
    path('productCategoryData/', productCategoryData, name='productCategoryData'),
    path('userData/', userData, name='userData'),
]
