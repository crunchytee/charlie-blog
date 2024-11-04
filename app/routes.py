from urllib.parse import urlparse
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm
from app.models import User, Post
from app.services.auth import login_helper, logout_helper, registration_helper
from app.services.posts import add_post, update_post, delete_post, view_post

# Main links that return a webpage
# Home Page
@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template("index.html", title="Home | Posts", posts=posts)

# Posts page - same as home page but added for continuity
@app.route('/posts')
def posts():
    return index()

# Create post
@app.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_post():
    return add_post()

# View post
@app.route('/post/<post_id>')
def post(post_id):
    return view_post(post_id)

@app.route('/post/<post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    return update_post(post_id)

@app.route('/post/<post_id>/delete', methods=['GET', 'POST'])
def remove_post(post_id):
    return delete_post(post_id)

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

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

