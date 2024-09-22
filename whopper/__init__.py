import os
from flask import Flask, render_template
from . import db

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='manilovefauna',
    DATABASE=os.path.join(app.instance_path, 'whopper.sqlite'),
)
db.init_app(app)
from . import auth, ticket, main
app.register_blueprint(auth.auth_bp)
app.register_blueprint(ticket.ticket_bp)
app.register_blueprint(main.main_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


