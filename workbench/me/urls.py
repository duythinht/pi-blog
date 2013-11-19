from django.conf.urls import patterns, url

from views import TrackView

urlpatterns = patterns(
    '',
    url(r'^$', TrackView.as_view(), name='me.tracks'),
)
