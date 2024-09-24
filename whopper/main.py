from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

main_bp = Blueprint('main', __name__)
@main_bp.route('/', methods=('GET', 'POST'))
def main():
    try:
        return render_template('index.html', winning_nums = current_app.winning_nums)
    except:
        return 'please reload after 1 minute'
