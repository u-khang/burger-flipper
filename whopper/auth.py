from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from whopper.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
    
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
    
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    # can't get scrypt to work use pbkdf2 instead
                    (username, generate_password_hash(password, 'pbkdf2'))
                )
                db.commit()
            except db.IntegrityError:
                return f"Username {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(f"flashing {error}")

    return render_template("auth/register.html") 



@bp.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error  = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        print(user)

        if user is None:
            error = 'Incorrect username.'
            print(error)
        elif not check_password_hash(user[2], password):
            error = 'Incorrect password.'
            print(error)
        
        if error is None:
            session.clear()
            session['user_id'] = user[0]
            return redirect(url_for('index'))

        flash(error)
    
    return render_template('auth/login.html')

