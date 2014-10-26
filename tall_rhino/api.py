from django.conf.urls import url, patterns, include
from blog.views import (
    ReadUpdateDeletePostAPIView, ListCreatePostAPIView, PublishPostAPIView)

urlpatterns = patterns(
    '',
    url(r'post/$', ReadUpdateDeletePostAPIView.as_view(),
        name='api-post'),
    url(r'post/(?P<pk>[\d]+)/$', ListCreatePostAPIView.as_view(),
        name='api-post'),
    url(r'publish/(?P<pk>[\d]+)/$', PublishPostAPIView.as_view(),
        name='api-publish'),
)
