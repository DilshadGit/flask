from datetime import datetime
from flask import Flask
from flask import (
    render_template,
    url_for,
    flash,
    redirect,
)

from flask_sqlalchemy import SQLAlchemy

from forms import UserRegistrationForm, UserLoginForm

from flask_bootstrap import Bootstrap

app = Flask(__name__)

# added securit key for csrf request and secure login detail
app.config[
    'SECRET_KEY'] = '8ba7aa2eea1ddbf6c024bea56ac6c804198b535a1fe5616cced1d0c61f21ddb2'
''' configurate the db and location '''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_db.db'

''' create the database '''
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    user_image = db.Column(db.String(50), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.user_image}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text(800), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.created_date}', '{self.author}')"

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
    template_name = 'registration/registration_form.html'
    form = UserRegistrationForm()
    if form.validate_on_submit():
        flash(f'You have been successfully registered for the username {form.username.data}',
              'success')
        return redirect(url_for('user_login'))
    context = {
        'title': 'Register',
    }
    return render_template(template_name, title='Register', form=form)


@app.route('/account/login', methods=['GET', 'POST'])
def user_login():
    template_name = 'registration/login_form.html'
    form = UserLoginForm()
    if form.validate_on_submit():
        if form.email.data == 'hello@gmail.com' and form.password.data == 'hello123':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful , please check the your detail', 'danger')
    return render_template(template_name, title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
