# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from samp1.models import Account
from django.http import HttpResponse
from django.views.generic import *
from django.views.generic.edit import *
from django.core.urlresolvers import reverse_lazy
from .forms import AccountForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
# Create your views here.


#class that generates Login form
class AccountLoginView(LoginView):
	model = Account
	# this applies the layout of form class
	form_class = LoginForm


	#redirect_authenticated_user = True

#class for validating if user is aready login
class BaseView(LoginRequiredMixin, View):

    def validate_user(self, user):
        if not user.is_active:
            return False
        return True

    def dispatch(self, request, *args, **kwargs):
    	if not self.validate_user(request.user):
        	logout(request)
        	return self.handle_no_permission()
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

#class for viewing all the account created
class AccountList(BaseView, ListView):
	model = Account

#class for insert items in database
class AccountInsert(BaseView, CreateView):
	model = Account
	success_url =reverse_lazy('account_list')
	form_class = AccountForm

	#function for creating a variable
	def get_context_data(self, **kwargs):        
		context = super(AccountInsert, self).get_context_data(**kwargs)        
		context['a'] = 2        
		return context

#class for updating items in database
class AccountUpdate(UpdateView):
	model = Account
	success_url =reverse_lazy('account_list')
	form_class = AccountForm
	
	def get_context_data(self, **kwargs):        
		context = super(AccountUpdate, self).get_context_data(**kwargs)        
		context['a'] = 1        
		return context

#class for deleting items in database
class AccountDelete(DeleteView):
	model = Account
	#this redirects the current url to account_list after successfully submitting
	success_url =reverse_lazy('account_list')