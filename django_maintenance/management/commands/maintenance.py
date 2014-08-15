""" Command to set maintenance status. """
from django.core.management.base import BaseCommand
import sys
import json
import os

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, '../../maintenance_settings.json')

class Command(BaseCommand):
    """ Set maintenance status """
    @classmethod
    def set_maintenance(cls, option):
    	""" Set maintenance status """
    	json_data = json.dumps({"DJANGO_MAINTENANCE": option},
    							indent=4, separators=(',', ': '))
    	json_file = open(JSON_FILE, 'w')
    	json_file.write(json_data)
    	json_file.close()

    def handle(self, *args, **kwargs):
    	""" Handle maintenance command """
    	# sys.argv mut be equal to 3
    	if len(sys.argv) != 3:
    		print 'Invalid number of arguments: {0}'.format(len(sys.argv) - 2)
    	# sys.argv[2] must have on or off
    	elif sys.argv[2] != 'on' and sys.argv[2] != 'off':
    		print 'Invalid maintenance option: {0}'.format(sys.argv[2])
    		print 'Valid options: on/off'
    	else:
    		self.set_maintenance(sys.argv[2])
