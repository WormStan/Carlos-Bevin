from flask import Blueprint

about_bp = Blueprint('about_bp', __name__)

@about_bp.route('/about')
def about():
    return "This is an example app"