from django.conf.urls import patterns, url

from views import EntryListView, EntryDetailView, TagView

urlpatterns = patterns(
    '',
    url(r'^$', EntryListView.as_view(), name='blog.entries'),
    url(r'^tags/(?P<tag>.+)/$', TagView.as_view(), name='blog.tags'),
    url(r'^(?P<pk>\d+)/$', EntryDetailView.as_view(), name='blog.detail')
)
