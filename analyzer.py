#-*- coding: utf-8 -*-

york1=[u' 빠가', u'10새', u'10새기', u'10새리', u'10세리', u'10쉐이', u'10쉑', u'10스', u'10쌔', u'10쌔기', u'10쎄', u'10알', u'10창', u'10탱', u'18것', u'18넘', u'18년', u'18노', u'18놈', u'18뇬', u'18럼', u'18롬', u'18새', u'18새끼', u'18색', u'18세끼', u'18세리', u'18섹', u'18쉑', u'18스', u'18아']
york2=[u'Fuck', u'ㅂㅅ', u'ㅅㅂ', u'ㅆ1발', u'ㅆㅂㄹㅁ', u'ㅆㅍ', u'ㅆ앙', u'ㅈㄹ', u'ㅗㅗㅗ', u'凸', u'갈보', u'갈보년', u'개같은', u'개구라', u'개년', u'개놈', u'개뇬', u'개대중', u'개돼중', u'개랄', u'개보지', u'개뿔', u'개새', u'개새기', u'개새끼', u'개새키', u'개색기', u'개색끼', u'개색키', u'개색히', u'개섀끼', u'개세']
york3=[u'개세끼', u'개세이', u'개소리', u'개쇳기', u'개수작', u'개쉐', u'개쉐리', u'개쉐이', u'개쉑', u'개쉽', u'개스끼', u'개시키', u'개십새기', u'개십새끼', u'개쐑', u'개쑈', u'개씹', u'개아들', u'개자슥', u'개자지', u'개접', u'개좌식', u'개허접', u'게색기', u'게색끼', u'광뇬', u'구녕', u'구멍', u'그년', u'그새끼']
york4=[u'놈현', u'뇬', u'눈깔', u'뉘뮈', u'뉘미럴', u'니귀미', u'니기미', u'니미', u'니아배', u'니아베', u'니아비', u'니어매', u'니어메', u'니어미', u'닝기리', u'닝기미', u'대가리', u'뎡신', u'도라이', u'돈놈', u'돌아이', u'돌은놈', u'되질래', u'뒈져', u'뒈져라', u'뒈진', u'뒈진다', u'뒈질', u'뒤질래', u'등신', u'디져라']
york5=[u'디진다', u'디질래', u'딩시', u'따식', u'때놈', u'또라이', u'똘아이', u'뙈놈', u'뙤놈', u'뙨넘', u'뙨놈', u'뚜쟁', u'뛰발', u'띄발', u'띠ㅋ발', u'띠바', u'띠발', u'띠불', u'띠팔', u'메친넘', u'메친놈', u'미췬', u'미친', u'바랄년', u'바보새끼', u'벼엉신', u'병쉰', u'병신', u'부랄', u'부럴', u'불알', u'불할', u'붕가']
york6=[u'뷰웅', u'븅', u'븅신', u'빌어먹', u'빙신', u'빠구리', u'빠굴', u'빠큐', u'뻐큐', u'뻑큐', u'뽁큐', u'상넘이', u'상놈을', u'상놈의', u'상놈이', u'새갸', u'새꺄', u'새새끼', u'새키', u'색끼', u'생쑈', u'세갸', u'세꺄', u'세끼', u'섹스', u'소새끼', u'쉐기', u'쉐끼', u'쉐리', u'쉐에기', u'쉐키', u'쉑', u'쉣', u'쉨', u'쉬발']
york7=[u'쉬밸', u'쉬벌', u'쉬뻘', u'쉬펄', u'쉽알', u'시끼', u'시댕', u'시뎅', u'시랄', u'시발', u'시밤', u'시벌', u'시부랄', u'시부럴', u'시부리', u'시불', u'시브랄', u'시팍', u'시팔', u'시펄', u'심탱', u'십8', u'십라', u'십새', u'십새끼', u'십세', u'십쉐', u'십쉐이', u'십스키', u'십쌔', u'십창', u'십탱', u'십팔', u'싶알']
york8=[u'싸가지', u'싹아지', u'쌉년', u'쌍넘', u'쌍년', u'쌍놈', u'쌍뇬', u'쌔끼', u'쌕', u'쌩쑈', u'쌴년', u'썅', u'썅년', u'썅놈', u'썡쇼', u'써벌', u'썩을년', u'썩을놈', u'쎄꺄', u'쎄엑', u'쒸벌', u'쒸뻘', u'쒸팔', u'쒸펄', u'쓰바', u'쓰박', u'쓰발', u'쓰벌', u'쓰팔', u'씁새', u'씁얼', u'씌발', u'씌파', u'씨8', u'씨ㅋ발']
york9=[u'씨끼', u'씨댕', u'씨뎅', u'씨바', u'씨바랄', u'씨박', u'씨발', u'씨방', u'씨방새', u'씨방세', u'씨밸', u'씨밸넘', u'씨뱅', u'씨벌', u'씨벨', u'씨봉', u'씨봉알', u'씨부랄', u'씨부럴', u'씨부렁', u'씨부리', u'씨불', u'씨붕', u'씨브랄', u'씨빠', u'씨빨', u'씨뽀랄', u'씨앙', u'씨파', u'씨팍', u'씨팔', u'씨펄', u'씸년']
york10=[u'씸뇬', u'씸새끼', u'씹같', u'씹년', u'씹뇬', u'씹보지', u'씹새', u'씹새기', u'씹새끼', u'씹새리', u'씹세', u'씹쉐', u'씹스키', u'씹쌔', u'씹이', u'씹자지', u'씹질', u'씹창', u'씹탱', u'씹퇭', u'씹팔', u'씹할', u'씹헐', u'아가리', u'아갈이', u'아갈통', u'아구창', u'아구통', u'아굴', u'엠병', u'염병', u'엿같']
york11=[ u'옘병', u'옘빙', u'왜년', u'왜놈', u'욤병', u'육갑', u'은년', u'을년', u'이년', u'이새끼', u'이새키', u'이스끼', u'이스키', u'잡것', u'잡넘', u'잡년', u'잡놈', u'저년', u'저새끼', u'접년', u'젖밥', u'조까', u'조까치', u'조낸', u'조또', u'조랭', u'조빠', u'조쟁이', u'조지냐', u'조진다', u'조질래', u'조찐', u'존나']
york12=[ u'존나게', u'존니', u'존만', u'존만한', u'좀물', u'좁년', u'좆', u'주데이', u'주뎅', u'주뎅이', u'주둥아리', u'주둥이', u'주접', u'주접떨', u'쥐랄', u'쥐롤', u'쥬디', u'지랄', u'지럴', u'지롤', u'지미랄', u'짜식', u'짜아식', u'쪼다', u'쫍빱', u'찌랄', u'창녀', u'캐년', u'캐놈', u'캐스끼', u'캐스키', u'캐시키']
york13=[u'팔럼', u'퍽큐', u'호로놈', u'호로새끼', u'호로색', u'호로쉑', u'호로스까이', u'호로스키', u'후라들', u'후래자식', u'후레', u'후뢰']

york=york1+york2+york3+york4+york5+york6+york7+york8+york9+york10+york11+york12+york13

class Line:
    def __init__(self, time, user, data):
        self.times=time
        self.user=user
        self.data=data

    def septimes(self):
	self.day=str(self.times[:4])+u"년 "+str(int(self.times[4:6]))+u"월 "+str(int(self.times[6:8]))+u"일"
	self.time=self.times[8:10]+":"+self.times[10:]
	return self

class User:
    def __init__(self, name):
        self.name=name
        self.linenums=[]
        self.yorknums=[]
        self.words={}
        self.yorks={}
	self.words_=[]
	self.yorks_=[]
	self.cnum=0
	self.ynum=0
    def __self__(self):
	return self.name
 
    def add(self, thing, mode="w"):
        if mode=="y":
            if thing in self.yorks:
                self.yorks[thing]+=1
            else:
                self.yorks[thing]=1
        else:
            if thing in self.words:
                self.words[thing]+=1
            else:
                self.words[thing]=1

        
    def addline(self, idx, line):
        self.linenums.append(idx)
        words=line
	for x in york:
	    if x in line:
		self.add(x, "y")
		self.yorknums.append(idx)
        for i in [',', '.', ':', ';', '~', '?', '!', '/', '(', ')', '^', '<', '>']: #어절 분리하기
            words.replace(i, ' ')
        words=words.split()
        for j in range(len(words)): #조사 분리하기
            if len(words[j])>1 and words[j][-2:] in [u'에게', u'이다', u'에서', u'처럼', u'라고']:
                words[j]=words[j][:-2]
            elif words[j][-1] in [u'은', u'는', u'이', u'가', u'을', u'를', u'께', u'의', u'고']:
                words[j]=words[j][:-1]
        for word in words:
            self.add(word)
            
    def getynum(self):
        ynum=0
        for i in self.yorks.keys():
            ynum+=self.yorks[i]
        return ynum

    def make_data(self):
	self.words_=sorted(self.words.items(), key=lambda x:x[1], reverse=True)
	self.yorks_=sorted(self.yorks.items(), key=lambda x:x[1], reverse=True)
                



def linechk(lines, mobile):
    analized_line=[]
    day='00000000'
    if not mobile:
	for line in lines.split('\n'):
	    element=line.split()
	    if len(element)<4 :
		continue
	    if len(element)==6 and (element[0] and element[5] == "---------------") and element[1][4]==u'년' :
		day= element[1][0:4]+element[2][:-1].zfill(2)+element[3][:-1].zfill(2)
		continue
	    if len(element)==4 and element[0][-1]==u'년' and element[1][-1]==u'월' and element[2][-1]==u'일' and element[3][-2:]==u'요일':
		day=element[0][:4]+element[1][:-1].zfill(2)+element[2][:-1].zfill(2)
		continue
	    if element[0][0] !=u'[' or element[1][0] !=u'[' or element[0][-1] != u']' or element[2][-1] != u']' :
		continue
	    add=0
	    if element[1][2] is u'후' and element[2][:2] is not '12':
		add=12
	    time=str(int(element[2].split(':')[0])+add).zfill(2)+element[2][-3:-1]
	    analized_line.append(Line(day+time, element[0][1:-1], " ".join(element[3:])).septimes())
    else:
	for line in lines.split('\n'):
	    element=line.split()
	    if len(element)<6 :
		continue
	    if not (element[0][-1]==u'년' and element[1][-1]==u'월' and element[2][-1]==u'일' and element[3][0]==u'오' and element[4][-1]==u',' and ":" in element[6:]) :
		continue
	    day=element[0][:-1]+element[1][:-1].zfill(2)+element[2][:-1].zfill(2)
	    add=0
	    if element[3][-1]==u'후' and element[4][:2] is not '12' :
		add=12
	    time=str(int(element[4][:-4])+add).zfill(2)+element[4][-3:-1]
	    cIdx=element[6:].index(':')+6
	    analized_line.append(Line(day+time, " ".join(element[5:cIdx]), " ".join(element[cIdx+1:])).septimes())
	    
    return analized_line, peoplechk(analized_line)


def peoplechk(lines):
    people={}
    names=[]
    idx=0
    for line in lines:
        if line.user not in names:
            names.append(line.user)
            people[line.user]=User(line.user)
        people[line.user].addline(idx, line.data)
        idx+=1
    for name in names:
        people[name].cnum=len(people[name].linenums)
        people[name].ynum=people[name].getynum()
	people[name].yorknums=sorted(list(set(people[name].yorknums)))
	people[name].make_data()
    return people
