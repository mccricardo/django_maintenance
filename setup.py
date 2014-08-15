from setuptools import setup, find_packages

version = '0.1.dev0'

setup(
    name = 'django_maintenance',
    packages = packages=find_packages(exclude=['test_app', 'django_maintenance_project']),
    version = version,
    download_url = 'https://github.com/mccricardo/django_maintenance/tarball/0.1.dev0'
    )