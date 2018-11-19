import os
import secrets

from PIL import Image

from flask import current_app, url_for
from flask_mail import Message
from flaskpro import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + file_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/images/profile_picture', picture_fn)

    resize_img = (140, 140)
    new_img = Image.open(form_picture)
    new_img.thumbnail(resize_img)
    new_img.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Reset Password Request',
                  sender='noreply@demo.com', recipients='user.email')
    msg.body = f'''
        To reset the password, please following the link: {url_for('reset_token', token=token,
            _external=True)}
        If you did not make this request then ignore this email and no change will make.
    '''
    mail.send(msg)
