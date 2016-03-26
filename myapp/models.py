from myapp import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Unicode)
  email = db.Column(db.Unicode, unique=True)

# Create the database tables.
db.create_all()
