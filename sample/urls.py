"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from samp1.forms import LoginForm
from samp1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url for login page
    url(r'^login/$', auth_views.login, {'template_name': 'samp1/login.html', 'authentication_form' : LoginForm }, name='login'),
    #url for logout button
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^$', views.AccountList.as_view(), name='account_list'),
    url(r'^insert$', views.AccountInsert.as_view(), name='account_insert'),
    url(r'^update/(?P<pk>\d+)$', views.AccountUpdate.as_view(), name='account_update'),
    url(r'^delete/(?P<pk>\d+)$', views.AccountDelete.as_view(), name='account_delete'),
]
