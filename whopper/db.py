import sqlite3, click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('fries.db')
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('fries are frying.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
