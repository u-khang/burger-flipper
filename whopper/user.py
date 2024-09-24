from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

user_bp = Blueprint('user', __name__)
@user_bp.route('/user', methods=('GET', 'POST'))
def user():
    if request.method == 'POST':

        error = None

        if error is None:
            return ''

        print(error)
        flash(error)

    return render_template('user.html')
