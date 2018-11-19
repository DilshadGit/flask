from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    template_name = 'errors/404.html'
    return render_template(template_name), 404


@errors.app_errorhandler(403)
def error_403(error):
    template_name = 'errors/403.html'
    return render_template(template_name), 403


@errors.app_errorhandler(500)
def error_500(error):
    template_name = 'errors/500.html'
    return render_template(template_name), 500
