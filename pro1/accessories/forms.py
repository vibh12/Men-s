from django import forms
from django.forms import ModelForm
from accessories.models import accessories

class accessories_form(forms.ModelForm):
	class Meta:
		model = accessories
		fields = '__all__'