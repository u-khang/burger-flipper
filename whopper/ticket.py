from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from whopper.db import get_db

ticket_bp = Blueprint('ticket', __name__)
@ticket_bp.route('/ticket', methods=('GET', 'POST'))
def ticket():
    if request.method == 'POST':
        n1 = request.form['n1']
        n2 = request.form['n2']
        n3 = request.form['n3']
        # db = get_db()
        # error = None

        # print(session['user_id'])
        # print(type(n1))
        # print(f"{n1}{n2}{n3}")

        # if error is None:
        #     print(session['user_id'])
        #     db.execute(
        #         "INSERT INTO ticket (user_id, numbers) VALUES (?, ?)",
        #         (session['user_id'], f"{n1}{n2}{n3}")
        #     )
        #     db.commit()
        return redirect(url_for('ticket.ticket'))

    return render_template('ticket.html')