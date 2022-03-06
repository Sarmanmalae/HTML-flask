from random import randint

from flask import Flask, url_for, request, render_template
from werkzeug.utils import redirect

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<name>')
@app.route('/index/<name>')
def index(name):
    n = name
    return render_template('base.html', title=n)


@app.route('/training/<string:prof>')
def ex2(prof):
    for i in [i.lower() for i in prof.split()]:
        if i in ['инженер', 'строитель']:
            t = 'ИНЖЕНЕРНЫЕ ТРЕНАЖЕРЫ'
        elif i in ['врач', 'ученый']:
            t = 'НАУЧНЫЕ СИМУЛЯТОРЫ'
        else:
            t = 'ТРЕНАЖЕРЫ ДЛЯ ОСТАЛЬНЫХ'
    return render_template('ex2.html', title=t)


@app.route('/list_prof/<string:ll>')
def ex3(ll):
    print(ll)
    return render_template('ex3.html', title='Mars', ll=ll)


@app.route('/answer')
@app.route('/auto_answer')
def ex4():
    data = {
        'title': 'info',
        "surname": "Watney",
        'name': 'Mark',
        'education': 'выше среднего',
        'prof': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def ex6():
    astrs = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тэдди Сандерс", "Шон Бин"]
    return render_template('ex6.html', title='Mars', a=astrs)


@app.route('/table/<string:sex>/<int:age>')
def ex7(sex, age):
    c = randint(0, 200)
    if sex == 'male':
        color = [c, c, 255]
    else:
        color = [255, c, c]
    print(color)
    return render_template('ex7.html', title='Mars')


@app.route('/test')
def test():
    return render_template('test.html', title='Mars', list2=["1", "1", "1", "1", "1"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
