from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from blog.views import BlogView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tall_rhino.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', BlogView.as_view(), name='home')
)
