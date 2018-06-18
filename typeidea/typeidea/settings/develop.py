# coding:utf-8

from .base import *  # NOQA
# class DebugWrapper(object):
#     def __getitem__(self, name):
#         return True
#
#     def __setitem__(self, name, value):
#         print(name, value)
#
#     def __getattr__(self, name):
#         print(name)
#         return True
#
#     def __setattr__(self, name, value):
#         print(name, value)
#
#     def __bool__(self):
#         return True


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

