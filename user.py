from flask import Blueprint, render_template
from forms import RegisterForm, LoginForm
user_bp = Blueprint('users', __name__, url_prefix='/user')


@user_bp.route('/')
def home_user():
    reg_url = '<br><a href="/user/register">Зарегистрироваться</a></br>'
    login_url = '<br><a href="/user/login">Вход</a></br>'
    return f'Привет выберите действия {reg_url + login_url}'


@user_bp.route('/register')
def register_user():
    # Назначить переменную для связки с формой
    form = RegisterForm()
    return render_template('register.html', form=form)


@user_bp.route('/login')
def login_user():
    form = LoginForm()
    return render_template('login.html', form=form)
