# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm, PasswordInput
from django import forms

# Create your models here.

class Account(models.Model):

	fname = models.CharField("First Name", max_length=50)
	mname = models.CharField("Middle Name", max_length=50)
	lname = models.CharField("Last Name", max_length=50)
	user = models.CharField("User", max_length=50)
	password = models.CharField("Password", max_length=50)

	class Meta:
		db_table = "sampledb"

class AccountForm(ModelForm):
	class Meta:
		model = Account
		fields = ('fname', 'mname', 'lname', 'user', 'password')

		widgets = {
            'password': PasswordInput(attrs={'size': '38'}),
        }