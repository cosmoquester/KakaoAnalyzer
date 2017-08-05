#-*- coding: utf-8 -*-


class Line:
    def __init__(self, time, user, data):
        self.time=time
        self.user=user
        self.data=data

class user:
    def __init__(self, name):
    	self.name=name
    	self.linenums=[]
    	self.yorknums=[]
    	self.words={}
    	self.yorks={}

def linechk(lines):
    analized_line=[]
    day='00000000'
    for line in lines.split('\n'):
        element=line.split()
        if len(element)<4 :
           continue
        if len(element)==6 and (element[0] and element[5] == u"---------------") and element[1][4]==u'년' :
            day= element[1][0:4]+element[2][:-1].zfill(2)+element[3][:-1].zfill(2)
            continue
        if ((element[0][0] or element[1][0]) !=u'[') or ((element[0][-1] or element[2][-1]) != u']' ) :
            continue
        add=0
        if element[1][2]==u'후':
            add=12
        time=str(int(element[2].split(':')[0])+add).zfill(2)+element[2][-3:-1]
        analized_line.append(Line(day+time, element[0][1:-1], u" ".join(element[3:])))
    return analized_line

