# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class accessories(models.Model):
	formal_watches = models.IntegerField(null=True, blank=True)
	formal_watches_Range = models.IntegerField(null=True, blank=True)
	digital_watches = models.IntegerField(null=True, blank=True)
	digital_watches_Range = models.IntegerField(null=True, blank=True)
	backpacks = models.IntegerField(null=True, blank=True)
	backpacks_Range = models.IntegerField(null=True, blank=True)
	laptop_backpack = models.IntegerField(null=True, blank=True)
	laptop_backpack_Range = models.IntegerField(null=True, blank=True)
	travelbags = models.IntegerField(null=True, blank=True)
	travelbags_Range = models.IntegerField(null=True, blank=True)
	sunglasses = models.IntegerField(null=True, blank=True)
	sunglasses_Range = models.IntegerField(null=True, blank=True)
	