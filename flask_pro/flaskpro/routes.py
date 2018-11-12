import os
import secrets

from PIL import Image

from flask import (
    render_template,
    url_for,
    flash,
    redirect,
    request,
)
from flaskpro import app, db, bcrypt
from flaskpro.forms import UserRegistrationForm, UserLoginForm, UpdateUserAccountForm
''' The models must imported after database created not before !!!! '''
from flaskpro.models import User, Post
from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required,
)

''' 
route in flask use to map to different pages, and decorator in flask use to add 
additional functionality to existing function and in this case this a Prout decorator 
will handle all of the complicated back-end
'''


posts = [
    {
        'title': 'Python',
        'author': 'Dilshad Abdulla',
        'content': "route in flask use to map to different pages, and decorator in flask use to add\
                    additional functionality to existing function and in this case this a Prout decorator \
                    will handle all of the complicated back-end",
        'publish_date': 'November 11 2018'
    },
    {
        'title': 'Google',
        'author': 'Dilshad Abdulla',
        'content': "route in flask use to map to different pages, and decorator in flask use to add\
                    additional functionality to existing function and in this case this a Prout decorator \
                    will handle all of the complicated back-end",
        'publish_date': 'April 12 2016'
    },
    {
        'title': 'Djnago',
        'author': 'Dilshad Abdulla',
        'content': "route in flask use to map to different pages, and decorator in flask use to add\
                    additional functionality to existing function and in this case this a Prout decorator \
                    will handle all of the complicated back-end",
        'publish_date': 'January 3 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    template_name = 'index.html'
    return render_template(template_name, title='Home', posts=posts)


@app.route('/about')
def about():
    template_name = 'about.html'
    return render_template(template_name, title='About us')


@app.route('/account/register', methods=['GET', 'POST'])
def user_register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    template_name = 'registration/registration_form.html'
    form = UserRegistrationForm()
    if form.validate_on_submit():
        ''' We ducrypte the password '''
        hashed_pwd = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_pwd)
        ''' Adding user to the database '''
        db.session.add(user)
        db.session.commit()
        flash(f'You have been successfully registered. You are ready to login', 'success')
        return redirect(url_for('user_login'))
    context = {
        'title': 'Register',
    }
    return render_template(template_name, title='Register', form=form)


@app.route('/account/login', methods=['GET', 'POST'])
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    template_name = 'registration/login_form.html'
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Unsuccessful , please check the your detail', 'danger')
    return render_template(template_name, title='Login', form=form)


@app.route('/account/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + file_ext
    picture_path = os.path.join(
        app.root_path, 'static/images/profile_picture', picture_fn)

    resize_img = (140, 140)
    new_img = Image.open(form_picture)
    new_img.thumbnail(resize_img)
    new_img.save(picture_path)

    return picture_fn


@app.route('/user/account', methods=['GET', 'POST'])
@login_required
def account():
    template_name = 'registration/user_account.html'
    form = UpdateUserAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.user_image = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been update!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    user_image = url_for(
        'static', filename='images/profile_picture/' + current_user.user_image)
    return render_template(template_name, title='account', user_image=user_image, form=form)
