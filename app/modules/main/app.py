from flask import Blueprint, render_template, request, jsonify

# Initiate blueprint
main_blueprint = Blueprint('main', __name__, template_folder='templates', url_prefix="/")


@main_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html', page="world")


@main_blueprint.route('/signup', methods=['GET'])
def signup():
    return render_template('index.html', page="signup")


@main_blueprint.route('/login', methods=['GET'])
def login():
    return render_template('index.html', page="login")


@main_blueprint.route('/main', methods=['GET'])
def main():
    return render_template('index.html', page="main")