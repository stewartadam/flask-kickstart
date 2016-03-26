import flask
import flask.ext.restless

from myapp import app, db
from myapp.models import User

# Create the Flask-Restless API manager.
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
