import dj_database_url
import django_heroku

from todo.settings.base import *


DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    # Use SQLITE for testing
    'TEST': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testing.sqlite'
    }
}

db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())

'''
# Load database settings from DATABASE_URL envvar
db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())

AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'blog.storage_backends.MediaStorage'
MEDIA_ROOT = "/media/"
'''