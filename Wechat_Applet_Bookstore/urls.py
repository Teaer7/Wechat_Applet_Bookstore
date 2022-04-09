"""Wechat_Applet_Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    url('admin/', admin.site.urls),
    url('users/', include('users.urls', namespace='users')),
    url('carts/', include('carts.urls', namespace='carts')),
    url('books/', include('books.urls', namespace='books')),
    url('orders/', include('orders.urls', namespace='orders')),
]
