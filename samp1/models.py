# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):

	fname = models.CharField("First Name", max_length=50)
	mname = models.CharField("Middle Name", max_length=50)
	lname = models.CharField("Last Name", max_length=50)
	user = models.CharField("User", max_length=50)
	password = models.CharField("Password", max_length=50)

	class Meta:
		db_table = "sampledb"
