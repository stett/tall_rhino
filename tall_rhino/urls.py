from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from blog.views import BlogView, PostView, EditBlogView, EditPostView

urlpatterns = patterns('',

    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # Blog posts
    url(r'^$', BlogView.as_view(), name='home'),
    url(r'^(?P<pk>[\d]+)/$', PostView.as_view(), name='post'),

    # Post editing
    url(r'^edit/$', EditBlogView.as_view(), name='edit'),
    url(r'^edit/(?P<pk>[\d]+)/$', EditPostView.as_view(), name='edit'),

    # API
    url(r'^api/', include('tall_rhino.api')),
)

if settings.DEBUG:
    urlpatterns += patterns('',

        # Serve static files if debugging
        url(r'media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

        # Load the browsable REST API
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    )
