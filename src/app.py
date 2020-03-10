# -*- coding: utf-8 -*-
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from functions import *

app = Flask(__name__)
app.api_host = os.getenv('API_HOST', 'api_host')
app.secret_key = os.urandom(12)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    games = get_games(host=app.api_host)
    return render_template('index.html', games=games)

@app.route('/login', methods=['POST'])
def do_login():
    cookie = get_login_cookie(username=request.form['username'], password=request.form['password'], host=app.api_host)
    if cookie:
        session['logged_in'] = True
        session['username'] = request.form['username']
        session['cookie'] = cookie
        return index()
    else:
        flash('Wrong Username or Password!')
        return index()

@app.route('/logout')
def do_logout():
        flash('Logged out!')
        session.clear()
        return index()

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/mygames')
def mygames():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('mygames.html')


@app.route('/newgame')
def newgame():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('newgame.html')


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
