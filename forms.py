from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired
# форма для регистрации


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Заполните имя!')])
    mail = EmailField('Почта', validators=[DataRequired('Заполните почту')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните пароль')])
    confirm_password = PasswordField('Повтор пароля', validators=[DataRequired('Повторно введите пароль')])
    button = SubmitField('Зарегестрироваться')


class LoginForm():
    mail = EmailField('Почта', validators=[DataRequired('Заполните почту')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните пароль')])

    button = SubmitField('Войти')