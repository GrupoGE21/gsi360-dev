from .base import *

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["api.seudominio.com"])
