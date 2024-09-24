from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
# from whopper.db import get_db

# from whopper.ticket import generate_winning_nums
# import threading, time
# from datetime import datetime


# def drawing_loop():
#     while True:
#         winning_nums = generate_winning_nums()
#         print(winning_nums[0])
#         # db = get_db()
#         # error = None

#         # if error is None:
#         #     db.execute(
#         #         "INSERT INTO drawing (user_id, numbers) VALUES (?, ?)",
#         #         (session['user_id'], f"{n1}{n2}{n3}")
#         #     )
#         #     db.commit()
#         #     return redirect(url_for('ticket.ticket'))

#         # print(error)
#         # flash(error)


#         time.sleep(5)

# thread = threading.Thread(target=drawing_loop)
# thread.daemon = True
# thread.start()




main_bp = Blueprint('main', __name__)
@main_bp.route('/', methods=('GET', 'POST'))
def main():
    return render_template('index.html', winning_nums = current_app.winning_nums)