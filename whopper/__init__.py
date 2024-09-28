import os
from flask import Flask, render_template, current_app, g
from . import db


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='manilovefauna',
    DATABASE=os.path.join(app.instance_path, 'whopper.sqlite'),
)

db.init_app(app)
from . import auth, ticket, main, user
app.register_blueprint(auth.auth_bp)
app.register_blueprint(ticket.ticket_bp)
app.register_blueprint(main.main_bp)
app.register_blueprint(user.user_bp)


from whopper.ticket import generate_winning_nums
import threading, time
from datetime import datetime, timedelta


def drawing_loop():
    while True:
        now = datetime.now()
        next_minute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
        delay = (next_minute - now).total_seconds()
        time.sleep(delay)

        with app.app_context():
            winning_nums = generate_winning_nums()
            print(f"lottery drawn at {datetime.now()}")
            current_app.winning_nums = winning_nums
            my_db = db.get_db()
            error = None

            if error is None:
                my_db.execute(
                    "INSERT INTO drawing (draw_date, winning_nums) VALUES (?, ?)",
                    (datetime.now(),''.join(map(str, winning_nums)))
                )
                my_db.commit()

            # print(error)
            # flash(error)


thread = threading.Thread(target=drawing_loop)
thread.daemon = True
thread.start()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user")
def user():
    return render_template("user.html")

