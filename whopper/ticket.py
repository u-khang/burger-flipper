from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import random
from datetime import datetime
from whopper.db import get_db

ticket_bp = Blueprint('ticket', __name__)
@ticket_bp.route('/ticket', methods=('GET', 'POST'))
def ticket():
    if request.method == 'POST':
        n1 = request.form['n1']
        n2 = request.form['n2']
        n3 = request.form['n3']
        db = get_db()
        error = None

        if n1 == n2 or n1 == n3 or n2 == n3:
            error = "numbers cannot repeat"

        if error is None:
            db.execute(
                "INSERT INTO ticket (user_id, date_obtained, numbers) VALUES (?, ?, ?)",
                (session['user_id'], datetime.now(), f"{n1}{n2}{n3}")
            )
            db.commit()
            return redirect(url_for('ticket.ticket'))

        print(error)
        flash(error)

    return render_template('ticket.html')

def generate_winning_nums():
    random_list = random.sample(range(10), 3)
    random_tuple = tuple(random_list)
    print(random_tuple)
    return random_tuple