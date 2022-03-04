from flask import Flask, url_for, request, render_template

app = Flask(__name__)


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
    print(t)
    return render_template('ex2.html', title=t)


@app.route('/test')
def test():
    return render_template('ex2.html', username='Kirill', title='Марс')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
