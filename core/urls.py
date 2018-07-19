"""Approapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout




urlpatterns = [
    url(r'^$', views.home),
    url(r'^blog1$', views.blog1),
    url(r'^blog2$', views.blog2),
    url(r'^blog3$', views.blog3),
    url(r'^blog4$', views.blog4),
    url(r'^products$', views.products),
    url(r'^mainpage/', views.mainpage),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'core/logout.html'}, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^profile/', views.profile_view, name='profile_view'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^verify/', views.search1, name="search"),
]