import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# Configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'secret'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

h = os.getenv('IP', '0.0.0.0')
p = int(os.getenv('PORT', 8080))

if __name__ == '__main__':
    app.run(host=h,port=p,debug=True)