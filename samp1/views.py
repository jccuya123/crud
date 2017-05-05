# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from samp1.models import Account
from django.http import HttpResponse
from django.views.generic import *
from django.views.generic.edit import *
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class AccountList(ListView):
	model = Account

class AccountInsert(CreateView):
	model = Account
	success_url =reverse_lazy('account_list')
	fields = ['fname', 'mname', 'lname', 'user', 'password']

class AccountUpdate(UpdateView):
	model = Account
	success_url =reverse_lazy('account_list')
	fields = ['fname', 'mname', 'lname', 'user', 'password']

class AccountDelete(DeleteView):
	model = Account
	success_url =reverse_lazy('account_list')