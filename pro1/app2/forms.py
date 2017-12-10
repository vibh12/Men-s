from django import forms
from django.forms import ModelForm
from app2.models import clothing

class clothing_form(forms.ModelForm):
	class Meta:
		model = clothing
		fields = '__all__'