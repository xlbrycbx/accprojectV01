from flask import Blueprint, request, render_template, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    return render_template('index.html')

@user_bp.route('/home')
def home():
    return render_template('home.html')

@user_bp.route('/base')
def base():
    return render_template('base.html')

@user_bp.route('/signup',methods=['POST','GET'])
def signup():
    msg = ''
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get(('repassword'))
        if password == repassword:
            user = User()
            user.username = username
            user.email = email
            user.password = generate_password_hash(password)
            db.session.add(user)
            db.session.commit()
            return render_template('login.html')
        else:
            msg = '两次输入不一致'
            return render_template('signup.html', msg=msg)

    else:
        return render_template('signup.html',msg=msg)

@user_bp.route('/login',methods=['POST','GET'])
def login():
    msg = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter(User.email == email).first()
        flag = check_password_hash(user.password, password)
        if flag:
            # session['username'] =user.username
            return render_template('home.html',user=user)
        else:
            msg = '用户名或密码输入错误'
            return render_template('login.html',msg=msg)
    else:
        return render_template('login.html')

@user_bp.route('/checkEmail')
def check_email():
    email = request.args.get('email')

    if User.query.filter(email == User.email).all():
        return jsonify(code=400, msg='此邮箱已被注册')
    else:
        return jsonify(code=200, msg='此邮箱可以注册')