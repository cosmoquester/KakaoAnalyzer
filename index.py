#-*- coding: utf-8 -*-

from datetime import datetime
from flask import render_template, Flask, request
import analyzer

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
    analedline, people=analyzer.linechk(request.form["data"])
#    for i in people.keys():
#	print(people[i].name+" "+str(people[i].ynum*1.0/people[i].cnum))
    names=sorted(people.keys(),key=lambda x:people[x].cnum, reverse=True)
    ynames=sorted(people.keys(), key=lambda x:people[x].ynum*1.0/people[x].cnum, reverse=True)
    values = []
    for i in names:
	values.append(people[i].cnum)
    values_y = []
    for i in ynames:
	values_y.append(people[i].ynum)
    colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC", "#FE2EC8 ", "#01DF01 ", "#B43104 ", "#FA8258 ", "#D8F781 ", "#642EFE ", "#58FAAC ", "#00FF00 ", "#0B4C5F" ]
    while len(colors)<len(names):
	colors.append('#000000')
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
     app.run(host='0.0.0.0', port=5000)
