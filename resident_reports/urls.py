from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^residentreports/$', views.rindex, name='rindex'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^allreports/$', views.allreports, name='allreports'),
    url(r'^new_report/(?P<topic_id>\d+)/$', views.new_report, name='new_report'),
    url(r'^edit_report/(?P<report_id>\d+)/$', views.edit_report, name='edit_report')
]
