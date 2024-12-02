from flask import render_template
from flask_login import login_required
from app import app
from app.services.auth import login_helper, logout_helper, registration_helper
from app.services.posts import add_post, update_post, delete_post, view_post, like_post_helper, dislike_post_helper, like_comment_helper, dislike_comment_helper, view_posts
from app.services.contact import contact_handler

# Main links that return a webpage
# Home Page
@app.route('/')
@app.route('/index')
def index():
    return view_posts()

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
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    return view_post(post_id)

# Edit post
@app.route('/post/<post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    return update_post(post_id)

# Delete post
@app.route('/post/<post_id>/delete', methods=['GET', 'POST'])
def remove_post(post_id):
    return delete_post(post_id)

# Auth
# Log In
@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_helper()

# Log Out
@app.route('/logout')
def logout():
    return logout_helper()

# Register New User
@app.route('/register', methods=['GET', 'POST'])
def register():
    return registration_helper()

# Static Pages
# About Page
@app.route('/about')
def about():
    return render_template("about.html", title="About")

# Credits Page
@app.route('/credits')
def credits():
    return render_template("credits.html", title="Credits")

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return contact_handler()

# 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Functional routes
# React to Posts
@app.route('/post/<post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    return like_post_helper(post_id)

@app.route('/post/<post_id>/dislike', methods=['POST'])
@login_required
def dislike_post(post_id):
    return dislike_post_helper(post_id)

# React to Comments
@app.route('/comment/<comment_id>/like', methods=['POST'])
@login_required
def like_comment(comment_id):
    return like_comment_helper(comment_id)

@app.route('/comment/<comment_id>/dislike', methods=['POST'])
@login_required
def dislike_comment(comment_id):
    return dislike_comment_helper(comment_id)

