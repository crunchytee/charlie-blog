from urllib.parse import urlparse
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from app import app, db
from app.forms import LoginForm, RegistrationForm, PostForm
from app.models import User, Post
from app.services.auth import is_user_valid

def add_post():
    
    # Post request, handle post creation
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            body_html = form.body_html.data,
            user_id = current_user.id,
            likes = 0,
            dislikes = 0
            )
        db.session.add(post)
        db.session.commit()
        flash("Posted!")
        return redirect(url_for("index"))
    
    # Get request, show add post form
    return render_template("add_post.html", title="Add Post", form=form)

def update_post(post_id):
    # Check for no post / authentication issue
    post = Post.query.filter_by(id=post_id).first()

    if post is None or not is_user_valid(post.user_id):
        flash("Oops! You can't do that. Try logging in.")
        return redirect(url_for("index"))
    
    # Post request, handle post creation
    form = PostForm()
    if form.validate_on_submit():
        print(form.title.data)
        post.title = form.title.data
        post.body_html = form.body_html.data
        db.session.commit()
        flash("Post Updated!")
        return redirect(url_for("index"))

    # Get request, show update post form. Post information is handed to template to be prefilled
    return render_template("update_post.html", title="Update Post", form=form, post=post)

# Delete posts