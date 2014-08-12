from django.conf.urls import patterns, url

from .views import IndexView, AboutView

urlpatterns = patterns('',
	url(r'^$', view=IndexView.as_view(), name='index'),	
    url(r'^about/$', view=AboutView.as_view(), name='about'),	
)