# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app2.forms import clothing_form
# Create your views here.
def cloth(request):
	form = clothing_form()
	if request.method == "POST":
		form = clothing_form(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'app2/clothing.html',{'form':clothing_form()})