from flask import render_template, flash, redirect, url_for, jsonify, request
from app import mail
from app.forms import ContactForm
from flask_mail import Message

def contact_handler():
    form = ContactForm()
    # Post request, handle contact form
    if form.validate_on_submit():
        message = format_message(form)
        subject = "New Chalie Blog Contact"
        send_email_internal(subject, message)
        flash("Message Sent!")
        return redirect(url_for("index"))
    
    # Get request, show contact form page
    return render_template("contact.html", title="Contact", form=form)

    
def send_email_internal(subject, body):
    
    # Create a Message object with subject, sender, and recipient list
    msg = Message(subject=subject,
                  sender='charlieblog916@example.com',
                  recipients=["snuswhistle@gmail.com"],
                  html=body
                  ) 
    
    # Send the email
    mail.send(msg)

def send_email_external(subject, body, send_to_address):
    
    # Create a Message object with subject, sender, and recipient list
    msg = Message(subject=subject,
                  sender='charlieblog916@example.com',
                  recipients=[str(send_to_address)],
                  html=body
                  ) 
    
    # Send the email
    mail.send(msg)

def format_message(form):
    return render_template("message.html", form=form)