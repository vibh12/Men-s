# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class clothing(models.Model):
	polos_and_tees = models.IntegerField(null=True,blank=True)
	polos_and_tees_Range = models.IntegerField(null=True,blank=True)
	casual_Shirts = models.IntegerField(null=True,blank=True)
	casual_Shirts_Range = models.IntegerField(null=True,blank=True)
	formal_Shirts = models.IntegerField(null=True,blank=True)
	formal_Shirts_Range = models.IntegerField(null=True,blank=True)
	sweaters = models.IntegerField(null=True,blank=True)
	sweaters_Range = models.IntegerField(null=True,blank=True)
	cardigans = models.IntegerField(null=True,blank=True)
	cardigans_Range = models.IntegerField(null=True,blank=True)
	jackets = models.IntegerField(null=True,blank=True)
	jackets_Range = models.IntegerField(null=True,blank=True)
	hoodies = models.IntegerField(null=True,blank=True)
	hoodies_Range = models.IntegerField(null=True,blank=True)
	denims = models.IntegerField(null=True,blank=True)
	denims_Range = models.IntegerField(null=True,blank=True)
	trousers = models.IntegerField(null=True,blank=True)
	trousers_Range = models.IntegerField(null=True,blank=True)
	shorts_and_34ths = models.IntegerField(null=True,blank=True)
	shorts_and_34ths_Range = models.IntegerField(null=True,blank=True)
	trackpants = models.IntegerField(null=True,blank=True)
	trackpants_Range = models.IntegerField(null=True,blank=True)
	suits = models.IntegerField(null=True,blank=True)
	suits_Range = models.IntegerField(null=True,blank=True)

	
