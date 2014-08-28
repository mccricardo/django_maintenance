django-under-maintenance
===============

Django middleware to put your application under maitenance. It works on a applicaton level, so your django aplication need to be running.

Installation
===============
 - Install django-under-maintenance
 - Add to your middleware classes

    MIDDLEWARE_CLASSES = (
    
    'django.middleware.common.CommonMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'django.middleware.doc.XViewMiddleware',
    
    'django_maintenance.maintenance.DjangoMaintenance',
    
    )
    
- Add the app:
    
    INSTALLED_APPS = (
    
    'django.contrib.admin',
    
    'django.contrib.auth',
    
    'django.contrib.contenttypes',
    
    ...,

    'django_maintenance',
    
    )

Commands
===============

  -  manage.py maintenance (on|off) - will (enable|dsable) maintenance mode.
 