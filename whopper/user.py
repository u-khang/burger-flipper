from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from whopper.db import get_db

user_bp = Blueprint('user', __name__)
@user_bp.route('/user', methods=('GET', 'POST'))
def user():
    db = get_db()

    try:
        user_tickets = db.execute(
            'SELECT * FROM ticket WHERE user_id = ?', (str(g.user[0]))
        ).fetchall()
    except:
        return 'uh oh something happened'
    

    if request.method == 'POST':
        error = None
        if error is None:
            return ''
        print(error)
        flash(error)

    return render_template('user.html', user_tickets = user_tickets)