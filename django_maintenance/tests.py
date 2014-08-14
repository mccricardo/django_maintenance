""" Test module for django_maintenance middleware. """
from django.test import TestCase
from django.core.urlresolvers import reverse
from .management.commands.maintenance import Command

class TestMaintenance(TestCase):        
    def test_maintenance_off_index(self):
        Command.set_maintenance('off')
        response = self.client.get(reverse('test_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the Index file!")
    
    def test_maintenance_off_about(self):
        Command.set_maintenance('off')
        response = self.client.get(reverse('test_app:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the About file!")
    
    def test_maintenance_on_index(self):
        Command.set_maintenance('on')
        response = self.client.get(reverse('test_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains (response, "This is the Index file!")
        self.assertContains(response, "Under maintenance!")
    
    def test_maintenance_on_about(self):
        Command.set_maintenance('on')
        response = self.client.get(reverse('test_app:about'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains (response, "This is the About file!")
        self.assertContains(response, "Under maintenance!")
