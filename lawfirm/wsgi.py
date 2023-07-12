"""
WSGI config for lawfirm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import environ

from django.core.wsgi import get_wsgi_application

environ.Env.read_env()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lawfirm.settings')

application = get_wsgi_application()

app = application
