from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'duythinht.views.home', name='home'),
    url(r'^blog/', include('workbench.blog.urls')),
    url(r'^', include('workbench.me.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
