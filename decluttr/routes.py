from flask import render_template, url_for, flash, redirect, request, session, g, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from decluttr import app, db, bcrypt
from datetime import datetime
from sqlalchemy.exc import IntegrityError


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

