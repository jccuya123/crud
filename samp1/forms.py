# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm
from .models import Account
from django.contrib.auth.forms import AuthenticationForm
# Create your models here.

class AccountForm(ModelForm):
	class Meta:
		model = Account
		fields = ('fname', 'mname', 'lname', 'user', 'password')

		widgets = {
			'fname': forms.TextInput(attrs={'size':'36'}),
			'mname': forms.TextInput(attrs={'size':'34'}),
			'lname': forms.TextInput(attrs={'size':'37'}),
			'user': forms.TextInput(attrs={'size':'44'}),
            'password': forms.PasswordInput(attrs={'size': '38'}, render_value = True),
        }


#login form for user
class LoginForm(AuthenticationForm):

    username = forms.CharField(max_length=254, 

        widget=forms.TextInput(

            attrs={'size': '30', 'class': 'form-control', 'placeholder' : 'Username', 'autofocus' : 'true'}))

    password = forms.CharField(strip=False, 

        widget=forms.PasswordInput(

            attrs={'size': '30', 'class': 'form-control', 'placeholder' : 'Password'}))