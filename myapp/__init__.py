import flask
import flask.ext.sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = 'a very long random string'

db = flask.ext.sqlalchemy.SQLAlchemy(app)

from myapp import api
from myapp import views
from myapp import models
