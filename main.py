from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<name>')
@app.route('/index/<name>')
def index(name):
    n = name
    return render_template('base.html', title=n)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
