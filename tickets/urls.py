from django.conf.urls import url
import views

urlpatterns = [
    url(r'^bug/list/$', views.bug_list, name='bug_list'),
    url(r'^bug/list/(?P<id>\d+)/$', views.bug_detail),
    url(r'^bug/newbug/$', views.new_bug, name='new_bug'),
    url(r'^bug/list/(?P<id>\d+)/edit$', views.edit_bug),
    url(r'^bug/newftr/$', views.new_feature, name='new_feature'),
]
