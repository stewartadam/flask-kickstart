import flask_restless

from myapp import app, db
from myapp.models import User

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(User, methods=['GET', 'POST', 'DELETE'])

# For more complex APIs use flask_restful, e.g.: https://github.com/mmautner/simple_api
