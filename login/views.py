from flask import render_template, flash, redirect,session,url_for,request,g
from flask_login import login_user,logout_user,current_user,login_required
from .forms import LoginForm
from app import app, db
from .models import User, ROLE_USER, ROLE_ADMIN


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'User' } #выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])