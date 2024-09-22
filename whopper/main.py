from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from whopper.db import get_db

main_bp = Blueprint('main', __name__)
@main_bp.route('/', methods=('GET', 'POST'))
def main():
    winning_nums = (7,3,0)
    g.winning_nums = winning_nums
    return render_template('index.html')