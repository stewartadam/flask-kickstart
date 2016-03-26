from myapp import app
from flask import redirect, render_template

@app.route('/')
def index():
    return render_template('index.html')
