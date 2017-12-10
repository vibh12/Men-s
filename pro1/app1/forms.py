from django import forms
from django.forms import ModelForm
from app1.models import shoes

class shoes_form(forms.ModelForm):
	class Meta:
		model = shoes
		fields = '__all__'