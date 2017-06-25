"""importing for flask."""
from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "sosecretive"


@app.route('/')
def home():
    print 'your home'
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    print 'you did it'
    name = request.form['name']
    location = request.form['location']
    language = request.form['favorite']
    comments = request.form['comments']
    if len(name) < 1 and len(comments) < 1:
        flash('error in name')
        flash('what no comments')
        return redirect('/')
    elif len(name) < 1:
        flash('error in name')
        return redirect('/')
    elif len(comments) < 1:
        flash('what no comments')
        return redirect('/')
    elif len(comments) > 120:
        flash(' whoa now, please keep comments under 120 characters ')
        return redirect('/')
    return render_template(
        'success.html', name=name, local=location,
        favLang=language, comment=comments)


app.run(debug=True)
