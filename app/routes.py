from urllib.parse import urlparse
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm
from app.models import User
from app.services.auth import login_helper, logout_helper, registration_helper
from app.services.posts import add_post

# Main links that return a webpage
@app.route('/')
@app.route('/index')
def index():
    return render_template("base.html", title="Home | Posts")

@app.route('/posts')
def posts():
    #TODO update template
    return render_template("base.html", title="Home | Posts") 

@app.route('/posts/create')
@login_required
def create_post():
    #TODO update template
    return add_post()

@app.route('/post/<post_id>')
def post(post_id):
    #TODO update template
    return render_template("base.html", title="Home | Posts")

# Auth
@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_helper()

@app.route('/logout')
def logout():
    return logout_helper()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return registration_helper()

@app.route('/about')
def about():
    #TODO update template
    return render_template("base.html", title="Home | Posts")

@app.route('/credits')
def credits():
    #TODO update template
    return render_template("base.html", title="Home | Posts")

@app.route('/contact')
def contact():
    #TODO update template
    return render_template("base.html", title="Home | Posts")

# Functional routes
@app.route('/post/<post_id>/like')
@login_required
def like_post(post_id):
    #TODO update template
    return render_template("base.html", title="Home | Posts")

@app.route('/post/<post_id>/dislike')
@login_required
def dislike_post(post_id):
    #TODO update template
    return render_template("base.html", title="Home | Posts")

@app.route('/post/<post_id>/comment')
@login_required
def comment(post_id):
    #TODO update template
    return render_template("base.html", title="Home | Posts")

