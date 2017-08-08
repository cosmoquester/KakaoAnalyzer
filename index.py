#-*- coding: utf-8 -*-

from datetime import datetime
from flask import render_template, Flask, request
from random import shuffle
import analyzer, codecs, time

app = Flask(__name__, static_url_path = "/static", static_folder = "static")


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='KakaoTalk Analyzer',
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


@app.route('/Analyze')
def Analyze():
    """Renders the contact page."""
    return render_template(
        'Analyze.html',
        title='Analyze',
        year=datetime.now().year,
        message='Copy, Paste And Click Button!'
    )

@app.route('/Analyzing', methods=['POST'])
def Analyzing():
    f=codecs.open("./log/"+str(time.time()), 'w', 'utf-8')
    f.write(request.form["data"])
    f.close()
    analedline, people=analyzer.linechk(request.form["data"], request.form.get('mobile'))
    names=sorted(people.keys(),key=lambda x:people[x].cnum, reverse=True)
    ynames=sorted(people.keys(), key=lambda x:people[x].ynum*1.0/people[x].cnum, reverse=True)
    values = []
    for i in names:
	values.append(people[i].cnum)
    values_y = []
    for i in ynames:
	values_y.append(people[i].ynum)
    colors = [ "#58ACFA", "#46BFBD", "#FDB45C", "#FEDCBA","#0101DF", "#DDDDDD", "#FE2E9A", "#FFFF00", "#00FF00", "#FF0040", "#FA8258 ", "#D8F781 ", "#642EFE ", "#58FAAC ", "#00FF00 ", "#0B4C5F" ]
    shuffle(colors)
    while len(colors)<len(names):
	colors.append('#FFFFFF')
    return render_template(
	'result.html', 
	title='Result', 
	year=datetime.now().year,
	people=people,
	names=names,
	ynames=ynames,
	set=zip(values, names, colors),
	set_y=zip(values_y, ynames, colors),
	lines=analedline,
    )


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
