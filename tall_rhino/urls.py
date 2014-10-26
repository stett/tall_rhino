from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from tall_rhino.views import (
    BlogView, PostView, CommentsView, EditBlogView, EditPostView, AboutView)
from django.views.generic.base import RedirectView

urlpatterns = patterns(
    '',

    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # Blog posts
    url(r'^$', BlogView.as_view(), name='home'),
    url(r'^(?P<pk>[\d]+)/$', PostView.as_view(), name='post'),
    url(r'^edit/$', EditBlogView.as_view(), name='edit'),
    url(r'^edit/(?P<pk>[\d]+)/$', EditPostView.as_view(), name='edit'),

    # Legacy posts
    url(r'^blog/(?P<slug>[-\w\d]+)/$', 'tall_rhino.views.legacy_post_redirect',
        name='legacy-post'),
    url(r'^post/(?P<slug>[-\w\d]+)/$', 'tall_rhino.views.legacy_post_redirect',
        name='legacy-post'),

    # Comments
    url(r'^comments/(?P<pk>[\d]+)/$', CommentsView.as_view(), name='comments'),

    # Pages
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^archive/$', 'blog.views.archive_view', name='archive'),

    # API
    url(r'^api/', include('tall_rhino.api')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',

        # Serve static files if debugging
        url(r'media/(?P<path>.*)',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),

        # Load the browsable REST API
        url(r'^api-auth/',
            include('rest_framework.urls',
            namespace='rest_framework')),
    )
