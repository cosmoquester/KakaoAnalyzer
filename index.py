#-*- coding: utf-8 -*-

from datetime import datetime
from flask import render_template, Flask, request
import analizer

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='KakaoTalk Analizer',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Hello!'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Description & Usage'
    )

@app.route('/Analize')
def Analize():
    """Renders the contact page."""
    return render_template(
        'Analize.html',
        title='Analize',
        year=datetime.now().year,
        message='Copy, Paste And Click Button!'
    )

@app.route('/Analizing', methods=['POST'])
def Analizing():
    analedline, people=analizer.linechk(request.form["data"])
    print people
    for i in people.keys():
	print(people[i].name+" "+str(people[i].ynum)+" "+str(people[i].cnum))
    return request.form["data"]

if __name__ == '__main__':
     app.run(host='0.0.0.0')
