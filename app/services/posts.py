from urllib.parse import urlparse
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from app import app, db
from app.forms import LoginForm, RegistrationForm, PostForm
from app.models import User, Post

def add_post():
    
    # Post request, handle post creation
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            body_html = form.body_html.data,
            user_id = current_user,
            likes = 0,
            dislikes = 0
            )
        db.session.add(post)
        db.session.commit()
        flash("Posted!")
        return redirect(url_for("index"))
    
    # Get request, show add post form
    return render_template("add_post.html", title="Add Post", form=form)