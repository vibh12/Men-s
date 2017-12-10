# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class shoes(models.Model):
	# name = Shoes data
	sport_Shoes = models.IntegerField(null=True, blank=True)
	sport_Shoes_Range = models.IntegerField(null=True, blank=True)
	sneakers = models.IntegerField(null=True, blank=True)
	sneakers_Range = models.IntegerField(null=True, blank=True)
	casual_Shoes = models.IntegerField(null=True, blank=True)
	casual_Shoes_Range = models.IntegerField(null=True, blank=True)
	formal_Shoes = models.IntegerField(null=True, blank=True)
	formal_Shoes_Range = models.IntegerField(null=True, blank=True)
	sandal = models.IntegerField(null=True, blank=True)
	sandal_Range = models.IntegerField(null=True, blank=True)
	boots = models.IntegerField(null=True, blank=True)
	boots_Range = models.IntegerField(null=True, blank=True)
	floaters = models.IntegerField(null=True, blank=True)
	floaters_Range = models.IntegerField(null=True, blank=True)

	# def __str__(self):
	# 	return self.name