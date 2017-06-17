"""importing for flask."""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    print 'your home'
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    print 'you did it'
    name = request.form['name']
    location = request.form['location']
    language = request.form['favorite']
    comments = request.form['comments']
    return render_template(
        'success.html', name=name, local=location,
        favLang=language, comment=comments)


app.run(debug=True)
