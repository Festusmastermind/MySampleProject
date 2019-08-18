from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns=[
    #ex: /polls/
    url(r'^$', views.index, name='index'),

    # ex: /polls/id e.g =4/
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /polls/id e.g =4/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /polls/id e.g =4/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]