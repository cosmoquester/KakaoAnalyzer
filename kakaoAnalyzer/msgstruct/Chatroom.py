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
        self.tot_msg = 0
        self.tot_person = {}
        if not line_analyze:
            self.line_analyze = self.line_spliter

    def __len__(self):
        return len(self.talkdays)
    
    def __getitem__(self, idx):
        return self.talkdays[idx]

    def __str__(self):
        return repr(self) + ' Name:' + self.name

    def get_words(self):
        ''' Return dictionary word:count used in this chatroom. '''
        ret = {}
        for word in self._words:
            cnt = word.get_count(chatroom=self)
            ret[word.name] = cnt
        return ret

    def tot_person_rate(self):
        ''' Return tot_person rate '''
        ret = {k:cnt/self.tot_msg for k,cnt in self.tot_person.items()}
        ret = sorted(list(ret.items()), key = lambda x:x[1])
        ret.reverse()
        return ret

    def find_word(self, word, create=False):
        return self._words.find(word, create=create)

    def append(self, datetime, person_name, content):

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
        
    def line_spliter(self, line):
        ret = {}
        for word in line.split():
            ret[word] = ret.get(word, 0) + 1
        return ret
