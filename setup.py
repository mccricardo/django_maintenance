from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'django-under-maintenance',
    packages = find_packages(exclude=['test_app', 'django_maintenance_project']),
    version = version,
    description = 'Setting you site Under Maintenance.',
    author = 'Ricardo Castro',
    author_email = 'mcc.ricardo@gmail.com',
    download_url = 'https://github.com/mccricardo/django_maintenance',
    keywords = ['django', 'maintenance'],
    package_data={
      '': ['*.json', 'templates/django_maintenance/*.html'],
   	},
)