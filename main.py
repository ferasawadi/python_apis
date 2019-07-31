from sanic import Blueprint
from sanic import Sanic
from api.users import users

app = Sanic(__name__)
blueBrint = app.blueprint(users)

app.run(host='0.0.0.0', port=8000)
