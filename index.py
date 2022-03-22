from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



class LoginForm(FlaskForm):
    username1 = StringField('ID Астронавта', validators=[DataRequired()])
    password1 = PasswordField('Пароль Астронавта', validators=[DataRequired()])
    username2 = StringField('ID Капитана', validators=[DataRequired()])
    password2 = PasswordField('Пароль Капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Домашняя страница'
    return render_template('base.html', **param)


@app.route('/answer')
def answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Kushnarev'
    param['name'] = 'Aleksey'
    param['education'] = 'Yandex Lyceum'
    param['profession'] = 'Capitan'
    param['sex'] = 'M'
    param['motivation'] = 'Всегда мечтал на Марс'
    param['ready'] = 'True'

    return render_template('answer.html', **param)

@app.route('/distribution')
def distribution():
    param = {}
    param['title'] = 'Каюты'
    param['persons'] = ['Евгений', 'Андрей', 'Артур', 'Никита']
    return render_template('distribution.html', **param)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')