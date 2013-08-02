"""
WSGI config for traffpunkt_aalto project.
"""
import os, sys
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "traffpunkt_aalto.settings")

application = Cling(get_wsgi_application())
