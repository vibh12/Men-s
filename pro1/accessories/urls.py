from django.conf.urls import url
from accessories import views

app_name = 'accessories'

urlpatterns = [
	url(r'^$', views.accessory)
]