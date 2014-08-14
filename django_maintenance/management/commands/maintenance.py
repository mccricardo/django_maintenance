""" Command to set maintenance status. """
from django.core.management.base import BaseCommand
import sys
import json

JSON_FILENAME = 'django_maintenance/maintenance_settings.json'

class Command(BaseCommand):
    """ Set maintenance status """
    @classmethod
    def set_maintenance(cls, option):
    	""" Set maintenance status """
    	json_data = json.dumps({"DJANgo_MAINTENANCE": option},
    							indent=4, separators=(',', ': '))
    	json_file = open(JSON_FILENAME, 'w')
    	json_file.write(json_data)
    	json_file.close()
    
