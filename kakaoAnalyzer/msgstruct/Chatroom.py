from .Person import Person, People
from .Message import Message, Msgs
from .TalkDay import TalkDay
from .Word import Word, Words


class Chatroom:
    ''' Chatroom is a class having information about Msgs and People in a chatroom. '''
    def __init__(self, name, line_analyze=None):
        self.name = name
        self.talkdays = []
        self.people = People()
        self._words = Words()
        self._curses = Words()
        self.tot_msg = 0
        self.tot_person = {}
        self.tot_curse = 0
        self.tot_person_curse = {}
        self.line_analyze = None

        if line_analyze == 'Kkma':
            try:
                from konlpy.tag import Kkma
                self.kkma = Kkma()
                self.line_analyze = self.kkma_analyzer
            except:
                print("Please install konlpy packge.")
                line_analyze = None

        if not line_analyze:
            self.line_analyze = self.line_spliter

    def __len__(self):
        return len(self.talkdays)
    
    def __getitem__(self, idx):
        return self.talkdays[idx]

    def __str__(self):
        return repr(self) + ' Name:' + self.name

    def get_words(self, curse=False):
        ''' Return dictionary word:count used in this chatroom. '''
        ret = {}
        for word in self._words if not curse else self._curses:
            cnt = word.get_count(chatroom=self)
            ret[word.name] = cnt
        return ret

    def tot_person_rate(self):
        ''' Return tot_person rate '''
        ret = {k:cnt/self.tot_msg for k,cnt in self.tot_person.items()}
        ret = sorted(list(ret.items()), key = lambda x:x[1])
        ret.reverse()
        return ret

    def find_word(self, word, create=False, curse = False):
        if curse:
            return self._curses.find(word, create=create)
        else:
            return self._words.find(word, create=create)

    def append(self, datetime, person_name, content):

        # Curse List
        curse_list = [' 빠가', '10새', '10새기', '10새리', '10세리', '10쉐이', '10쉑', '10스', '10쌔', '10쌔기', '10쎄', '10알', '10창', '10탱', '18것', '18넘', '18년', '18노', '18놈', '18뇬', '18럼', '18롬', '18새', '18새끼', '18색', '18세끼', '18세리', '18섹', '18쉑', '18스', '18아',
        'Fuck', 'ㅂㅅ', 'ㅅㅂ', 'ㅆ1발', 'ㅆㅂㄹㅁ', 'ㅆㅍ', 'ㅆ앙', 'ㅈㄹ', 'ㅗㅗㅗ', '凸', '갈보', '갈보년', '개같은', '개구라', '개년', '개놈', '개뇬', '개대중', '개돼중', '개랄', '개보지', '개뿔', '개새', '개새기', '개새끼', '개새키', '개색기', '개색끼', '개색키', '개색히', '개섀끼', '개세',
        '개세끼', '개세이', '개소리', '개쇳기', '개수작', '개쉐', '개쉐리', '개쉐이', '개쉑', '개쉽', '개스끼', '개시키', '개십새기', '개십새끼', '개쐑', '개쑈', '개씹', '개아들', '개자슥', '개자지', '개접', '개좌식', '개허접', '게색기', '게색끼', '광뇬', '구녕', '구멍', '그년', '그새끼',
        '놈현', '뇬', '눈깔', '뉘뮈', '뉘미럴', '니귀미', '니기미', '니미', '니아배', '니아베', '니아비', '니어매', '니어메', '니어미', '닝기리', '닝기미', '대가리', '뎡신', '도라이', '돈놈', '돌아이', '돌은놈', '되질래', '뒈져', '뒈져라', '뒈진', '뒈진다', '뒈질', '뒤질래', '등신', '디져라',
        '디진다', '디질래', '딩시', '따식', '때놈', '또라이', '똘아이', '뙈놈', '뙤놈', '뙨넘', '뙨놈', '뚜쟁', '뛰발', '띄발', '띠ㅋ발', '띠바', '띠발', '띠불', '띠팔', '메친넘', '메친놈', '미췬', '미친', '바랄년', '바보새끼', '벼엉신', '병쉰', '병신', '부랄', '부럴', '불알', '불할', '붕가',
        '뷰웅', '븅', '븅신', '빌어먹', '빙신', '빠구리', '빠굴', '빠큐', '뻐큐', '뻑큐', '뽁큐', '상넘이', '상놈을', '상놈의', '상놈이', '새갸', '새꺄', '새새끼', '새키', '색끼', '생쑈', '세갸', '세꺄', '세끼', '섹스', '소새끼', '쉐기', '쉐끼', '쉐리', '쉐에기', '쉐키', '쉑', '쉣', '쉨', '쉬발',
        '쉬밸', '쉬벌', '쉬뻘', '쉬펄', '쉽알', '시끼', '시댕', '시뎅', '시랄', '시발', '시밤', '시벌', '시부랄', '시부럴', '시부리', '시불', '시브랄', '시팍', '시팔', '시펄', '심탱', '십8', '십라', '십새', '십새끼', '십세', '십쉐', '십쉐이', '십스키', '십쌔', '십창', '십탱', '십팔', '싶알',
        '싸가지', '싹아지', '쌉년', '쌍넘', '쌍년', '쌍놈', '쌍뇬', '쌔끼', '쌕', '쌩쑈', '쌴년', '썅', '썅년', '썅놈', '썡쇼', '써벌', '썩을년', '썩을놈', '쎄꺄', '쎄엑', '쒸벌', '쒸뻘', '쒸팔', '쒸펄', '쓰바', '쓰박', '쓰발', '쓰벌', '쓰팔', '씁새', '씁얼', '씌발', '씌파', '씨8', '씨ㅋ발',
        '씨끼', '씨댕', '씨뎅', '씨바', '씨바랄', '씨박', '씨발', '씨방', '씨방새', '씨방세', '씨밸', '씨밸넘', '씨뱅', '씨벌', '씨벨', '씨봉', '씨봉알', '씨부랄', '씨부럴', '씨부렁', '씨부리', '씨불', '씨붕', '씨브랄', '씨빠', '씨빨', '씨뽀랄', '씨앙', '씨파', '씨팍', '씨팔', '씨펄', '씸년',
        '씸뇬', '씸새끼', '씹같', '씹년', '씹뇬', '씹보지', '씹새', '씹새기', '씹새끼', '씹새리', '씹세', '씹쉐', '씹스키', '씹쌔', '씹이', '씹자지', '씹질', '씹창', '씹탱', '씹퇭', '씹팔', '씹할', '씹헐', '아가리', '아갈이', '아갈통', '아구창', '아구통', '아굴', '엠병', '염병', '엿같',
        '옘병', '옘빙', '왜년', '왜놈', '욤병', '육갑', '은년', '을년', '이년', '이새끼', '이새키', '이스끼', '이스키', '잡것', '잡넘', '잡년', '잡놈', '저년', '저새끼', '접년', '젖밥', '조까', '조까치', '조낸', '조또', '조랭', '조빠', '조쟁이', '조지냐', '조진다', '조질래', '조찐', '존나',
        '존나게', '존니', '존만', '존만한', '좀물', '좁년', '좆', '주데이', '주뎅', '주뎅이', '주둥아리', '주둥이', '주접', '주접떨', '쥐랄', '쥐롤', '쥬디', '지랄', '지럴', '지롤', '지미랄', '짜식', '짜아식', '쪼다', '쫍빱', '찌랄', '창녀', '캐년', '캐놈', '캐스끼', '캐스키', '캐시키',
        '팔럼', '퍽큐', '호로놈', '호로새끼', '호로색', '호로쉑', '호로스까이', '호로스키', '후라들', '후래자식', '후레', '후뢰']
        # Add new person
        cur_person = self.people.find(person_name)
        if not cur_person:
            new_person = Person(person_name)
            new_person.chatrooms.append(self)
            self.people.append(new_person)
            cur_person = new_person

        # Add new date
        if datetime.date() not in self.talkdays:
            new_talkday = TalkDay(datetime.year, datetime.month, datetime.day)
            self.talkdays.append(new_talkday)
            cur_talkday = new_talkday
        else:
            cur_talkday = self.talkdays[self.talkdays.index(datetime.date())]

        # Add new Message
        cur_msg = Message(self, cur_talkday, cur_person, datetime, content)
        self.tot_msg += 1
        self.tot_person[person_name] = self.tot_person.get(person_name, 0) + 1
        cur_talkday.append(self, cur_msg)
        
        # Sentence Analize
        line_words = self.line_analyze(content)
        for word in line_words:

            # Add word to chatroom and people
            cur_word = self.find_word(word, create=True)
            cur_person.add_word(cur_word)        

            # Add word history
            cur_word.append(cur_talkday, cur_person, self, cur_msg)  
        
            if word in curse_list:
                self.find_word(cur_word, create=True, curse=True)
                cur_person.add_word(cur_word, curse=True)
                self.tot_curse += 1
                self.tot_person_curse[person_name] = self.tot_person_curse.get(person_name, 0) + 1
                
    def line_spliter(self, line):
        ''' Just split a line into several parts '''
        ret = {}

        for i in [',', '.', ':', ';', '~', '/', '(', ')', '^', '<', '>']:
                line.replace(i, ' ')
        for word in line.split():
            if len(word)>1 and word[-2:] in ['에게', '이다', '에서', '처럼', '라고', '이가']:
                word=word[:-2]
            elif word[-1] in ['은', '는', '이', '가', '을', '를', '께', '의', '고']:
                word=word[:-1]
            ret[word] = ret.get(word, 0) + 1
        return ret

    def kkma_analyzer(self, line):
        ''' Analyze line using Kkma Analzyer '''
        ret = {}
        try:
            pos = self.kkma.pos(line)
        except:
            pos = []

        for w, p in pos:
            if p[0] in 'NVM' or p in ['XR', 'SL', 'EMO']:
                if p[0] == 'V':
                    w += '다'
                ret[w] = ret.get(w, 0) + 1
        return ret