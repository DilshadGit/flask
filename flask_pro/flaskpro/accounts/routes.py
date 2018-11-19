from flask import (
    render_template,
    url_for,
    flash,
    redirect,
    request,
    Blueprint,
)
from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required,
)
from flaskpro import db, bcrypt
''' The models must imported after database created not before !!!! '''
from flaskpro.models import User, Post

from flaskpro.accounts.forms import (
    UserRegistrationForm,
    UserLoginForm,
    UpdateUserAccountForm,
    RequestResetForm,
    RestPasswordForm,
)

from flaskpro.accounts.utils import save_picture, send_reset_email


accounts = Blueprint('accounts', __name__)


@accounts.route('/account/register', methods=['GET', 'POST'])
def user_register():
    if current_user.is_authenticated:
        return redirect(url_for('settings.home'))
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
        return redirect(url_for('accounts.user_login'))
    context = {
        'title': 'Register',
    }
    return render_template(template_name, title='Register', form=form)


@accounts.route('/account/login', methods=['GET', 'POST'])
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for('settings.home'))
    template_name = 'registration/login_form.html'
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('settings.home'))
        else:
            flash('Unsuccessful , please check the your detail', 'danger')
    return render_template(template_name, title='Login', form=form)


@accounts.route('/account/logout')
def logout():
    logout_user()
    return redirect(url_for('settings.home'))


@accounts.route('/user/account', methods=['GET', 'POST'])
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
        return redirect(url_for('accounts.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    user_image = url_for(
        'static', filename='images/profile_picture/' + current_user.user_image)
    return render_template(template_name, title='account', user_image=user_image, form=form)


@accounts.route('/user/reset_password', methods=['GET', 'POST'])
def reset_request():
    template_name = 'registration/reset_request.html'
    if current_user.is_authenticated:
        return redirect(url_for('settings.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has ben send to your email address with, please follow the process', 'info')
        return redirect(url_for('accounts.user_login'))
    return render_template(template_name, title='Reset Password', form=form)


@accounts.route('/user/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    template_name = 'registration/reset_token.html'
    if current_user.is_authenticated:
        return redirect(url_for('settings.home'))
    user = User.verify_reset_token(token)
    if not user:
        flash(f'This token is expired or invalid', 'warning')
        return redirect(url_for('accounts.reset_request'))
    form = RestPasswordForm()
    if form.validate_on_submit():
        ''' We ducrypte the password '''
        hashed_pwd = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        ''' Adding user to the database '''
        user.password = hashed_pwd
        db.session.commit()
        flash(f'You password has been updated. You are ready to login', 'success')
        return redirect(url_for('accounts.user_login'))
    return render_template(template_name, form=form, title='Reset new password')
