from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('test_app.urls', namespace='testapp')),
)
