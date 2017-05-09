# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm
from .models import Account

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