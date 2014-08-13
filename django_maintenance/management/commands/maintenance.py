""" Command to set maintenance status. """
from django.core.management.base import BaseCommand
import sys
import json

JSON_FILENAME = 'django_maintenance/maintenance_settings.json'

class Command(BaseCommand):
    """ Set maintenance status """
    pass