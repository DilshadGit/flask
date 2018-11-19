from flask import (
    Blueprint,
    render_template,
    request,
)
from flaskpro.models import Post


settings = Blueprint('settings', __name__)

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


@settings.route('/')
@settings.route('/home')
def home():
    template_name = 'index.html'
    return render_template(template_name, title='Home', posts=posts)


@settings.route('/about')
def about():
    template_name = 'about.html'
    return render_template(template_name, title='About us')
