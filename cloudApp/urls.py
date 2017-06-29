from django.conf.urls import url

from . import views

#app_name = 'cloudApp'
#urlpatterns = [
#    # ex: /cloudApp/
#    url(r'^$', views.index, name='index'),
#    # ex: /cloudApp/5/
#    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#    # ex: /cloudApp/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#    # ex: /cloudApp/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#]

app_name = 'cloudApp'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]