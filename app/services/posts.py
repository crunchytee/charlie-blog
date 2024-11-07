from urllib.parse import urlparse
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from app import app, db
from app.forms import LoginForm, RegistrationForm, PostForm, CommentForm
from app.models import User, Post, Comment
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
        post.title = form.title.data
        post.body_html = form.body_html.data
        db.session.commit()
        flash("Post Updated!")
        return redirect(url_for("index"))

    # Get request, show update post form. Post information is handed to template to be prefilled
    return render_template("update_post.html", title="Update Post", form=form, post=post)

def delete_post(post_id):
    # Check for no post / authentication issue
    post = Post.query.filter_by(id=post_id).first()

    if post is None or not is_user_valid(post.user_id):
        flash("Oops! You can't do that. Try logging in.")
        return redirect(url_for("index"))
    # First delete any associated comments with the post
    comments = Comment.query.filter_by(post_id=post_id)
    for comment in comments:
        db.session.delete(comment)
    # Then, delete post
    db.session.delete(post)
    db.session.commit()
    flash("Post Deleted")
    return redirect(url_for("index"))

def view_post(post_id):
    # Comment form
    form = CommentForm()
    print("reached view post", flush=True)
    if form.validate_on_submit():
        print("reached form validate", flush=True)
        print(post_id, flush=True)
        comment = Comment(post_id=int(post_id), comment=form.comment.data, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash("Comment added")
        # return redirect("/post/" + post_id)
        return redirect("/index")
    # Get post - return 404 if no post
    post = Post.query.filter_by(id=post_id).first_or_404()
    truncated_title = post.title if len(post.title) < 50 else (post.title[:47] + "...")
    return render_template("post.html", title=truncated_title, post=post, form=form)

# Delete posts