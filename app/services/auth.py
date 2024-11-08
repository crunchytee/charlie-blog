from urllib.parse import urlparse
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from app import db
from app.forms import LoginForm, RegistrationForm
from app.models import User

def login_helper():
    # Check if user is logged in. If so, take them to the homepage
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    # Login form handling
    form = LoginForm()
    if form.validate_on_submit():
        # Try and get user from database
        user = User.query.filter_by(username=form.username.data).first()

        # User not found or password incorrect -> notify user and return to login page
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
            return redirect(url_for("login"))
        
        # Log user in and redirect them to their desired page, or index if next not found
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlparse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    
    # User requesting login form, show login page
    return render_template("login.html", title="Login", form=form)

def logout_helper():
    # Log out user and send them back to the homepage
    logout_user()
    return redirect(url_for("index"))

def registration_helper():
    # Check if user is logged in. If so, take them to the homepage. They shouldn't be registering for an account if they're loggedn in already
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    # Post request, handle login
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful!")
        return redirect(url_for("login"))
    
    # Get request, show registration form
    return render_template("register.html", title="Registration", form=form)

# Safe user function. User has to be found and match current user
def is_user_valid(user_id):
    if current_user.is_anonymous:
        return False
    user = User.query.filter_by(id = user_id).first()
    if user is None or user.username != current_user.username:
        return False
    return True