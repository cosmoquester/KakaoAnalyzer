'''
Chatroom is a class having information about Msgs and People in a chatroom.
'''
class Chatroom:
    def __init__(self, name):
        self.name = name
        self._Msgs = []
        self.people = []
        self.words = []

    def append(self, msgs):
        self._Msgs.append(msgs)

    def __len__(self):
        return len(self._Msgs)
    
    def __getitem__(self, idx):
        return self._Msgs[idx]

    def getiter(self):
        ''' Return iterator having whole messages in this chatroom. '''

        for msgs in self._Msgs:
            for msg in msgs:
                yield msg

    def construct(self):
        ''' Reconstruct messages into formatted text '''

        ret = ''
        for msgs in self._Msgs:
            ret += 'Date Time'
            for msg in msgs:
                ret += 'Message'

        return ret