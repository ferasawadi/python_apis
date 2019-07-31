from sanic import Blueprint
from sanic.response import json
import sqlalchemy as db

user = Blueprint('users_controller')


@user.route('/show-user')
async def show(request):
    engine = db.create_engine('mysql+pymysql://hinet:12345678@localhost/notoer_db', pool_recycle=3600)
    connection = engine.connect()
    metadata = db.MetaData()
    users_table = db.Table('users', metadata, autoload=True, autoload_with=engine)
    query = db.select([users_table]).where(users_table.columns.phone_number == request.json['phone_number'])
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    # return json(result_set)
    return json({
        'status': True,
        'message': 'User Info',
        'data': {
            query.columns.id: result_set[0][0],
            query.columns.full_name: result_set[0][3],
            query.columns.email: result_set[0][5],
        }
    })


@user.route('/create-user')
async def store(request):
    if request.json['user'] is None:
        return json({'user is required'})
    return json({
        'message': 'User created Successfully!',
        'user': request.json['user']
    }, 201)
