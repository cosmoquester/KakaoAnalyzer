'''
A Word instance is a word like "apple".
It has information about who, when, how much use this.
'''
class Word:
    def __init__(self, name):
        self.name = name
        self._history = []

    def append(talkday, person, chatroom, message):
        self._history.append((talkday, person, chatroom, message))

    def __getitem__(self, idx):
        return self._history[idx]

    def get(talkday=None, person=None, chatroom=None):
        '''
        You can bring Word history using 'get' mothod.
        It returns Messages by iterator according to named parameter person or talkday.
        '''
        for t, p, c, m in self._history:
            if (not talkday or t == talkday) and\
                (not person or p is person) and\
                (not chatroom or c is chatroom):
                yield m
        
    def get_count(talkday=None, person=None, chatroom=None):
        '''
        You can bring Word usage count using 'get_count' mothod.
        It returns word count according to named parameter person or talkday.
        '''
        ret = 0

        for t, p, c, m in self._history:
            if (not talkday or t == talkday) and\
                (not person or p is person) and\
                (not chatroom or c is chatroom):
                ret += 1
        return ret