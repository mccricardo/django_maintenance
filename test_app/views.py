from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    """ Index View. """
    template_name = 'test_app/index.html'

class AboutView(TemplateView):
    """ About View. """
    template_name = 'test_app/about.html'
