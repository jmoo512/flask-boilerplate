from flask import current_app
from flask import render_template,request,Blueprint,redirect,url_for, request, jsonify

core = Blueprint('core',__name__)


#HOME

@core.route('/')
def index():
    return render_template('index.html')
