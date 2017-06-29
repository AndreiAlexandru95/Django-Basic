from django.conf.urls import url

from . import views

app_name = 'cloudApp'
urlpatterns = [
    # ex: /cloudApp/
    url(r'^$', views.index, name='index'),
    # ex: /cloudApp/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /cloudApp/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /cloudApp/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]