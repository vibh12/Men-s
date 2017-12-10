from django.conf.urls import url
from app2 import views

app_name = 'app2'

urlpatterns = [
	url(r'^$', views.cloth),
]