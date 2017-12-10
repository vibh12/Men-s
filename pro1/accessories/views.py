# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from accessories.forms import accessories_form
# Create your views here.
def accessory(request):
	form = accessories_form()
	if request.method == "POST":
		form = accessories_form(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'accessories/accessories.html',{'form':accessories_form()})