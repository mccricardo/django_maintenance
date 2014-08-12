""" Middleware to handle maintenace. """
from django.shortcuts import render_to_response
import json

JSON_FILENAME = 'django_maintenance/maintenance_settings.json'

class DjangoMaintenance(object):
    """ Django Maintennece middleware. """
    def process_request(self, request):
        """ Handle request. """

        # Read maintenace file
        json_data = open(JSON_FILENAME, 'r')
        data = json.load(json_data)
        json_data.close()

        # Check if maintenance mode is on. Render template if it is.
        if data['DJANGO_MAINTENANCE'] == 'on':
            return render_to_response('django_maintenance/maintenance.html')