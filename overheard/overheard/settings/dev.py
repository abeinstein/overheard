from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS += ('debug_toolbar',)

# DJANGO debug toolbar
DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = ('127.0.0.1',)