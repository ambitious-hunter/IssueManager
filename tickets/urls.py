from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views

import views

urlpatterns = [
    url(r'^bug/list/$', views.bug_list, name='bug_list'),
    url(r'^bug/list/(?P<id>\d+)/$', views.bug_detail),
    url(r'^bug/newbug/$', views.new_bug, name='new_bug'),
    url(r'^bug/list/(?P<id>\d+)/edit$', views.edit_bug),
    url(r'^bug/newftr/$', views.new_feature, name='new_feature'),
    url(r)
]
