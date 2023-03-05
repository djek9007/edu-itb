"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bajlanys/', views.Contact.as_view(), name='contact'),
    path('quzhattar/', views.Quzhattar.as_view(), name='quzhattar'),
    path('<slug:category_slug>/', views.PostList.as_view(), name='category_post'),
    path('<slug:category_slug>/<slug:slug>/', views.PostDetail.as_view(), name='detail_post'),

]

