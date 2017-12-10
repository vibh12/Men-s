# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.forms import shoes_form 
# Create your views here.
def shoe(request):
	form = shoes_form()
	if request.method == 'POST':
		form = shoes_form(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'app1/shoes.html', {'form':shoes_form()})
