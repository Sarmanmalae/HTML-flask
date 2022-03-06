from flask import Flask, url_for, request, render_template

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
    return render_template('ex3.html', ll=ll)


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

@app.route('/login')
def ex5():
    return render_template('login.html')


@app.route('/test')
def test():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
