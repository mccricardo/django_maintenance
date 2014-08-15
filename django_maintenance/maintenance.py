""" Middleware to handle maintenace. """
from django.shortcuts import render_to_response
import json
import os

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'maintenance_settings.json')

class DjangoMaintenance(object):
    """ Django Maintennece middleware. """
    def process_request(self, request):
        """ Handle request. """

        # Read maintenace file
        try:
            json_data = open(JSON_FILE, 'r')
            data = json.load(json_data)
            json_data.close()
        except IOError:
            # If settings file is missing default to None
            data = None


        # Check if maintenance mode is on. Render template if it is.
        if data and data['DJANGO_MAINTENANCE'] == 'on':
            return render_to_response('django_maintenance/maintenance.html')