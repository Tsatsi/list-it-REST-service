from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from resources import ItemResource, UserResource

api.add_resource(ItemResource, '/api/items', '/api/user/items/<int:id>', '/api/items/<int:id>')
api.add_resource(UserResource, '/api/user/register')
