from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from whopper.db import get_db

ticket_bp = Blueprint('ticket', __name__)
@ticket_bp.route('/ticket', methods=('GET', 'POST'))
def ticket():
    return render_template('ticket.html')