# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from samp1.models import Account
from django.http import HttpResponse
from django.views.generic import *
from django.views.generic.edit import *
from django.core.urlresolvers import reverse_lazy
from .forms import AccountForm
# Create your views here.

class AccountList(ListView):
	model = Account

class AccountInsert(CreateView):
	model = Account
	success_url =reverse_lazy('account_list')
	# fields = ['fname', 'mname', 'lname', 'user', 'password']
	form_class = AccountForm

	def get_context_data(self, **kwargs):        
		context = super(AccountInsert, self).get_context_data(**kwargs)        
		context['a'] = 2        
		return context

class AccountUpdate(UpdateView):
	model = Account
	success_url =reverse_lazy('account_list')
	#fields = ['fname', 'mname', 'lname', 'user', 'password']
	form_class = AccountForm
	
	def get_context_data(self, **kwargs):        
		context = super(AccountUpdate, self).get_context_data(**kwargs)        
		context['a'] = 1        
		return context

class AccountDelete(DeleteView):
	model = Account
	success_url =reverse_lazy('account_list')