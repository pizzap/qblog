"""
WSGI config for qblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import site
import sys

from django.core.wsgi import get_wsgi_application

site.addsitedir("/home/kishita/.pyenv2.7/lib/python2.7/site-packages/")
sys.path.append("/var/www/django/qblog")
sys.path.append("/var/www/django/qblog/qblog")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qblog.settings")

activate_env = os.path.expanduser("/home/kishita/.pyenv2.7/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

application = get_wsgi_application()

