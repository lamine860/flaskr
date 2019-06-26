import os 
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, render_template, abort, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='\xa9W\xa8\x846\x03\xf08\xf6\xbbo0\xe7)0B<\xeb\xf4.Nz\xe2\xda',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv



def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db();
    return g.sqlite_db   

@app.teardown_appcontext
def db_close(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()    



@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""

    init_db()
    print('Initialized the database.')