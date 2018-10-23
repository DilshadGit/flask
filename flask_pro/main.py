from flask import Flask
from flask import (
	render_template,
	url_for,
)

from flask_bootstrap import Bootstrap

app = Flask(__name__)


''' 
route in flask use to map to different pages, and decorator in flask use to add 
additional functionality to existing function and in this case this a Prout decorator 
will handle all of the complicated back-end
'''
@app.route('/')
@app.route('/home')
def home():
	template_name = 'index.html'
	return render_template(template_name, title='Home')


@app.route('/about')
def about():
	template_name = 'about.html'
	return render_template(template_name, title='About us')



if __name__ == '__main__':
	app.run(debug=True)
