from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^allreports/$', views.allreports, name='allreports'),
    url(r'^new_report/$', views.new_report, name='new_reports'),
    url(r'^edit_report/$', views.edit_report, name='edit_report')
]
