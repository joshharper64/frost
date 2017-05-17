from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^allreports/$', views.allreports, name='allreports'),
    url(r'^new_report/$', views.new_report, name='new_report'),
    url(r'^edit_report/(?P<report_id>\d+)/$', views.edit_report, name='edit_report'),
]
