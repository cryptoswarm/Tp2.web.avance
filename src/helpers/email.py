from threading import Thread
from email_validator import EmailUndeliverableError, validate_email
from flask import current_app, render_template
from flask_mail import Message
from src import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(
        app.config["DATA_SWARM_MAIL_SUBJECT_PREFIX"] + " " + subject,
        sender=app.config["MAIL_USERNAME"],
        recipients=[to],
    )
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


def validate_email_domain(email):
    try:
        validate_email(email, check_deliverability=True)
        return True
    except EmailUndeliverableError as err:
        return err.args
