from .common import *
import os

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG =False

ALLOWED_HOSTS = ['192.168.1.94','127.0.0.1','0.0.0.0']
