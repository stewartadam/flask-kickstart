import flask
import flask_sqlalchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = flask.Flask(__name__, instance_relative_config=True)
with app.app_context():
    limiter = Limiter(
      get_remote_address,
      app=app,
    )

    app.config.from_object('myapp.config.DefaultConfig')
    app.config.from_pyfile('myapp.cfg', silent=True)
    app.config.from_envvar('CONFIG_FILE', silent=True)

    db = flask_sqlalchemy.SQLAlchemy(app)

    from . import api
    from . import models
    from . import views
