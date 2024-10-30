from flask import render_template
from app import app#, db, posts
# from app.forms import LoginForm, RegistrationForm
# from app.models import User
# from app.posts import Posts

# Main links that return a webpage
@app.route('/')
@app.route('/index')
# @login_required
def index():
    return render_template("base.html", title="Home | Posts")

@app.route('/posts')
def posts():
    #TODO update template
    return render_template("base.html", title="Home | Posts") 

@app.route('/posts/create')
def create_post():
    #TODO update template
    return render_template("base.html", title="Home | Posts") 

@app.route('/post/<post_id>')
def post(post_id):
    #TODO update template
    return render_template("base.html", title="Home | Posts")

@app.route('/login')
def login():
    #TODO update template
    return render_template("base.html", title="Home | Posts")

@app.route('/register')
def register():
    #TODO update template
    return render_template("base.html", title="Home | Posts")

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
def like_post(post_id):
    #TODO update template
    return render_template("base.html", title="Home | Posts")

@app.route('/post/<post_id>/dislike')
def dislike_post(post_id):
    #TODO update template
    return render_template("base.html", title="Home | Posts")

@app.route('/post/<post_id>/comment')
def comment(post_id):
    #TODO update template
    return render_template("base.html", title="Home | Posts")

