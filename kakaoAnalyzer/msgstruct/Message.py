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

