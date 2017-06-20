from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^bug/list/$', views.bug_list, name='bug_list'),
    url(r'^bug/list/(?P<id>\d+)/$', views.bug_detail),
    url(r'^bug/newbug/$', views.new_bug, name='new_bug'),
    url(r'^bug/list/(?P<id>\d+)/edit$', views.edit_bug),
    url(r'^bug/newftr/$', views.new_feature, name='new_feature'),
    url(r'^bug/bug/withdraw_feature$', views.withdraw_feature_request),
    # url(r'^paypal-cancel', views.paypal_cancel),
]
