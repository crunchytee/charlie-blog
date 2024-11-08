from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username taken. Please use a different username.")

    def valitate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email taken. Please use a different email.")

class PostForm(FlaskForm):
    title = StringField("Post title", validators=[DataRequired(), Length(2, 300, "Post title must be within 2 and 300 characters")])
    body_html = TextAreaField("HTML post content", validators=[DataRequired(), Length(2, 30000, "Post must be within 2 and 30,000 characters")])
    banner_image = StringField("Banner image (optional)", validators=[Length(2, 300, "Banner image must be within 2 and 300 characters")])
    submit = SubmitField("Post")

class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", validators=[DataRequired(), Length(2, 300, "Post must be within 2 and 300 characters")])
    submit = SubmitField("Post Comment")