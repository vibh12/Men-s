from django.conf.urls import url
from app1 import views

app_name = 'app1'

urlpatterns = [
	url(r'^$', views.shoe),

]
	

