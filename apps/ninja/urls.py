from django.conf.urls import patterns, url, include     # import functions to match patterns
from . import views                    # import views.py file from our quiz app
urlpatterns = patterns('',
  # this url pattern matches empty string!!!
  url(r'^$', views.index, name='index'),
  url(r'^process_money/?$', views.process_money, name='process_money'),
  url(r'^reset/?$', views.reset, name='reset'),
  #  url(r'^interests/?$', views.interests, name='interests'),
  # url(r'^interests/(?P<user_id>\d+)', views.user, name='user'),

)
