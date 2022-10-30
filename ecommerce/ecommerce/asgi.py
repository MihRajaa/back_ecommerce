"""
ASGI config for ecommerce project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from tornado import httpserver
from tornado import ioloop
from tornado import wsgi

from django.core.wsgi import get_wsgi_application


def main():
    # path to your settings module
    os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce.settings'
    application = get_wsgi_application()
    container = wsgi.WSGIContainer(application)
    http_server = httpserver.HTTPServer(container)
    http_server.listen(8888)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# application = get_asgi_application()
