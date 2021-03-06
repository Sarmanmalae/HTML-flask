import json
import os
from random import randint, choice

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


@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        n = os.listdir('static/img/carousel')[1:]
        print()
        return render_template('new_carousel.html', photos=n)
    elif request.method == 'POST':
        t = request.files['file']
        a = len(os.listdir('static/img/carousel'))
        name = 'pic' + str(a + 1) + '.jpg'
        with open(f'static/img/carousel/{name}', 'wb') as f:
            f.write(t.read())
        print(1)
        n = os.listdir('static/img/carousel')[1:]
        return render_template('new_carousel.html', photos=n)


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


@app.route('/members')
def ex10():
    with open('templates/team.json', encoding='utf8') as team:
        data = json.load(team)
    a = randint(1, len(data))
    member = data[str(a)]
    member['specialities'] = ', '.join(member['specialities'])
    return render_template('members.html', title='Member', member=member)


@app.route('/table/<sex>/<age>')
def ex7(sex, age):
    c = randint(17, 150)
    if sex == 'male':
        color = [c, c, 255]
    else:
        color = [255, c, c]
    f_color = '#' + hex(color[0])[2:] + hex(color[1])[2:] + hex(color[2])[2:]
    pic_child = 'alien_c1.jpg'
    pic_parent = 'markw.jpg'
    if int(age) < 21:
        pic = pic_child
    else:
        pic = pic_parent
    pic = '/static/img/' + pic
    print(color, f_color)
    print(hex(color[0])[2:], hex(color[1])[2:], hex(color[2])[2:])
    return render_template('ex7.html', title='Mars', color=f_color, pic=pic)


@app.route('/test')
def test():
    return render_template('test.html', title='Mars', list2=["1", "1", "1", "1", "1"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
