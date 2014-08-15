from setuptools import setup, find_packages

version = '0.1.dev0'

setup(
    name = 'django_maintenance',
    packages = find_packages(exclude=['test_app', 'django_maintenance_project']),
    version = version,
    download_url = 'https://github.com/mccricardo/django_maintenance',
    package_data={
      'django_maintenance': ['templates/django_miantenance/*'],
   },
    )