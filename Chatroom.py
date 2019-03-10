from Person import Person, People
from Message import Message, Msgs
from TalkDay import TalkDay

'''
Chatroom is a class having information about Msgs and People in a chatroom.
'''
class Chatroom:
    def __init__(self, name):
        self.name = name
        self.talkdays = []
        self.people = People()
        self.words = []
        self.tot_msg = 0
        self.tot_person = {}

    def __len__(self):
        return len(self.talkdays)
    
    def __getitem__(self, idx):
        return self.talkdays[idx]

    def __str__(self):
        return repr(self) + ' Name:' + self.name

    def getiter(self):
        ''' Return iterator having whole messages in this chatroom. '''
        for msgs in self.talkdays:
            for msg in msgs:
                yield msg

    def get_words(self):
        ''' Return dictionary word:count used in this chatroom. '''
        ret = {}
        for word in words:
            cnt = word.get_count(chatroom=self)
            ret[word.name] = cnt
        return ret

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
        new_msg = Message(self, cur_talkday, cur_person, datetime, content)
        self.tot_msg += 1
        self.tot_person[person_name] = self.tot_person.get(person_name, 0) + 1
        cur_talkday.append(self, new_msg)
        
        # Sentence Analize

        # 


        # test code 
        # try:
        #     print(datetime.strftime('%y/%m/%d %H:%M:%S'), person_name, content)
        # except UnicodeEncodeError as e:
        #     print(e)



    def construct(self):
        ''' Reconstruct messages into formatted text '''

        ret = ''
        for msgs in self._Msgs:
            ret += 'Date Time'
            for msg in msgs:
                ret += 'Message'

        return ret