from flask import Blueprint, request, render_template, jsonify
from werkzeug.security import generate_password_hash

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/')
def index():
    return render_template('user/index.html')


@user_bp.route('/register', methods=['POST', 'GET'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
                user = User()
                user.username = username
                user.password = generate_password_hash(password)
                db.session.add(user)
                db.session.commit()
        else:
            msg = '两次输入不一致'
        return render_template('user/register.html', msg=msg)

    else:
        return render_template('user/register.html', msg=msg)


@user_bp.route('/checkUsername')
def check_username():
    username = request.args.get('username')

    if User.query.filter(username == User.username).all():
        return jsonify(code=400, msg='此用户名已被注册')
    else:
        return jsonify(code=200, msg='此用户名可以注册')
