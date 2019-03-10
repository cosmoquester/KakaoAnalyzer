class Person:
    def __init__(self, name):
        self.name = name
        self.words = []
        self.curses = []

    def get_words(self, talkday=None):
        ''' It returns dictionary the words and the number person used. '''
        ret = {}
        for word in self.words:
            cnt = word.get_count(talkday=talkday, person=self)
            if cnt:
                ret[word.name] = cnt
        return ret

    def get_curses(self, talkday=None):
        ''' It returns dictionary the curses and the number person used. '''
        ret = {}
        for word in self.curses:
            cnt = word.get_count(talkday=talkday, person=self)
            if cnt:
                ret[word.name] = cnt
        return ret