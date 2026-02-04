import sqlite3
from datetime import datetime
from flask import current_app, g
import click

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as schema:
        db.executescript(schema.read().decode("utf-8"))

@click.command("init-db")
def init_db_command():
    init_db()
    print("Initialized database")

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

sqlite3.register_converter("timestamp", lambda dt: datetime.fromisoformat(dt.decode()))
