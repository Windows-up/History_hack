from flask import render_template, Flask,request
from parser_html import parser_html
app = Flask(__name__)

URL = "https://obrazovaka.ru/test/biografiya-richarda-3-s-otvetami.html"

image, test_name, title, lesson, _class,answer = parser_html(URL)

result = f"{answer} правильных ответов из {answer}!"


@app.route('/')
def hello_world():

    return render_template("history.html", result=result, test_name=test_name, title=title, lesson=lesson, \
                           _class = _class, image=image, answers=answer, last_hour="-69")

@app.route('/test')
def parametr():
    result = request.args.get('result')
    test_name = request.args.get('test_name')
    title = request.args.get('title')
    lesson = request.args.get('lesson')
    _class = request.args.get('class')
    image = "https://obrazovaka.ru/" + request.args.get('image')
    answer = request.args.get('answer')
    last_hour = request.args.get('last_hour')
    return render_template("history.html", result=result, test_name=test_name, title=title, lesson=lesson, \
                           _class = _class, image=image, answers=answer, last_hour=last_hour)

app.run()