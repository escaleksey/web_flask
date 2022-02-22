from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')