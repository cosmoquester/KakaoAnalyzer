class Person:
    def __init__(self, name):
        self.name = name
        self.words = []
        self.curses = []
        self.chatrooms = []

    def __str__(self):
        return self.name

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

class People:
    def __init__(self):
        self._people = []

    def __len__(self):
        return len(self._people)

    def __getitem__(self, idx):
        return self._people[idx]

    def __str__(self):
        ret = "["
        for person in self._people:
            ret += str(person) + ", "
        ret = ret[:-2] + ']'

        return ret
    
    def append(self, person):
        return self._people.append(person)

    def names(self):
        for p in self._people:
            yield p.name
        
    def find(self, name):
        names = list(self.names())
        if name in names:
            return self._people[names.index(name)]
        else:
            return None