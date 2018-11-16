import os
import secrets

from PIL import Image

from flask import (
    render_template,
    url_for,
    flash,
    redirect,
    request,
    abort,
)
from flaskpro import app, db, bcrypt, mail
from flaskpro.forms import (
    UserRegistrationForm,
    UserLoginForm,
    UpdateUserAccountForm,
    CreatePostForm,
    UpdatePostForm,
    RequestResetForm,
    RestPasswordForm,
)
''' The models must imported after database created not before !!!! '''
from flaskpro.models import User, Post
from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required,
)
from flask_mail import Message

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
    },
    {
        'title': 'Bootstrap',
        'author': 'Dilshad Abdulla',
        'content': "route in flask use to map to different pages, and decorator in flask use to add\
                    additional functionality to existing function and in this case this a Prout decorator \
                    will handle all of the complicated back-end",
        'publish_date': 'November 11 2018'
    },
    {
        'title': 'AWS',
        'author': 'Dilshad Abdulla',
        'content': "route in flask use to map to different pages, and decorator in flask use to add\
                    additional functionality to existing function and in this case this a Prout decorator \
                    will handle all of the complicated back-end",
        'publish_date': 'April 12 2016'
    },
    {
        'title': 'Restframework API',
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


@app.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    template_name = 'post_create.html'
    form = CreatePostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'{post.title} has been successfully created.', 'success')
        return redirect(url_for('post_list'))
    return render_template(template_name, title='Create new post', form=form, legend='Create New post')


@app.route('/posts')
def post_list():
    template_name = 'posts.html'
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.created_date.desc()).paginate(page=page, per_page=3)
    return render_template(template_name, title='Post list', posts=posts)


@app.route('/post/<int:post_id>')
def post_detail(post_id):
    template_name = 'post_detail.html'
    post = Post.query.get_or_404(post_id)
    return render_template(template_name, post=post, title=post.title)


@app.route('/post/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_update(post_id):
    template_name = 'post_update.html'
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
        flash('Please be a ware that you only allowed to update own post!')
    form = UpdatePostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(f'{current_user.username.upper()}, Your current post has been updated', 'success')
        return redirect(url_for('post_detail', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template(template_name, title='Update Post', post=post, form=form, legend='Update Post')


@app.route('/post/delete/<int:post_id>', methods=['POST'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'{current_user.username.upper()}, Your current post has ben deleted', 'success')
    return redirect(url_for('post_list'))


@app.route('/user/<string:username>')
def user_posts(username):
    template_name = 'user_posts.html'
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(
        Post.created_date.desc()).paginate(page=page, per_page=3)
    return render_template(template_name, title='User Post list', posts=posts, user=user)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Reset Password Request', sender='noreply@demo.com', recipients='user.email')
    msg.body = f'''
        To reset the password, please following the link: {url_for('reset_token', token=token,
            _external=True)}
        If you did not make this request then ignore this email and no change will make.
    '''
    mail.send(msg)


@app.route('/user/reset_password', methods=['GET', 'POST'])
def reset_request():
    template_name = 'registration/reset_request.html'
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has ben send to your email address with, please follow the process', 'info')
        return redirect(url_for('user_login'))
    return render_template(template_name, title='Reset Password', form=form)


@app.route('/user/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    template_name = 'registration/reset_token.html'
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if not user:
        flash(f'This token is expired or invalid', 'warning')
        return redirect(url_for('reset_request'))
    form = RestPasswordForm()
    if form.validate_on_submit():
        ''' We ducrypte the password '''
        hashed_pwd = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        ''' Adding user to the database '''
        user.password = hashed_pwd
        db.session.commit()
        flash(f'You password has been updated. You are ready to login', 'success')
        return redirect(url_for('user_login'))
    return render_template(template_name, form=form, title='Reset new password')
