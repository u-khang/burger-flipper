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

@ticket_bp.route('/SCAN_TICKET')
def scan_ticket():
    # use queries to check ticket winnings. for js fetch calls. return # of matching nums

    ticket_id = request.args.get('ticket_id', default=None)
    db = get_db()

    drawing_data = db.execute('SELECT * FROM drawing ORDER BY draw_date').fetchall()
    ticket_data = db.execute(f'SELECT * FROM ticket WHERE ticket_id = {ticket_id}').fetchone()


    ticket_obtained_date = ticket_data[2]
    matched_drawing = ''

    for drawing in drawing_data:
        drawing_date = drawing[1]
        if drawing_date < ticket_obtained_date:
            continue
        else:
            matched_drawing = drawing
            break

    ticket_nums = ticket_data[3]
    drawing_nums = matched_drawing[2]
    num_matches = common_numbers(ticket_nums, drawing_nums)



    return f'{matched_drawing}\n{num_matches}'

def common_numbers(numstr1, numstr2):
    common_nums = set(numstr1) & set(numstr2)
    print(type(common_nums))
    return len(common_nums)