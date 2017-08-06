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
#    for i in people.keys():
#	print(people[i].name+" "+str(people[i].ynum*1.0/people[i].cnum))
    return render_template(
	'result_cnum.html', 
	title='Result', 
	year=datetime.now().year,
	people=people,
	message="Thanks",
	names=sorted(people.keys(),key=lambda x:people[x].cnum, reverse=True),
	ynames=sorted(people.keys(), key=lambda x:people[x].ynum*1.0/people[x].cnum, reverse=True),
    )


if __name__ == '__main__':
     app.run(host='0.0.0.0')
