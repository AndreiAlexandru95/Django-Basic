from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^S', views.index, name='index'),
]