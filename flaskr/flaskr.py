import os 
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, render_template, abort, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config(['DATABASE']))
    rv.row_factory = sqlite3.Row
    return rv



@app.route('/')
def home():
    return 'SALut'