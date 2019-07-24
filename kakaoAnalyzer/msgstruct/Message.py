class Message:
    '''
    Message is one message someone talked.
    talkday is a class having Messages in some day and datetime is just datetime.
    '''
    def __init__(self, chatroom, talkday, person, datetime, content):
        self.chatroom = chatroom
        self.talkday = talkday
        self.person = person
        self.datetime = datetime
        self.content = content

    def __str__(self):
        return ' '.join((self.datetime.strftime("%Y-%m-%d %H:%M"), self.person.name, self.content))

    def to_string(self, form='%D %T %N %C'):
        '''
        This function will return msg into fommatted string.
        You can use [%D, %T, %N, %C, %R]
        %D : Date
        %T : Time
        %N : Person Name
        %C : Content
        %R : Chatroom Name
        '''
        form = form.replace('%D', self.datetime.strftime("%Y-%m-%d"))
        form = form.replace('%T', self.datetime.strftime("%H:%M"))
        form = form.replace('%N', self.person.name)
        form = form.replace('%C', self.content)
        form = form.replace('%R', self.chatroom.name)

        return form

class Msgs:
    '''
    A Msgs is a collection of Messages by specific chatroom and talkday.
    '''
    def __init__(self, chatroom, talkday):
        self.chatroom = chatroom
        self.talkday = talkday
        self._msgs = []

    def append(self, message):
        self._msgs.append(message)
    
    def __len__(self):
        return len(self._msgs)

    def __getitem__(self, idx):
        return self._msgs[idx]

