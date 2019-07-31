from .UserController import user
from sanic import Blueprint

users = Blueprint.group(user, url_prefix='users')
