from .base import *

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="localhost,127.0.0.1").split(",")

