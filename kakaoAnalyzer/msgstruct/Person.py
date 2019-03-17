from .Word import Words

class Person:
    '''
    It is about a person. It is distinguished by name.
    It has Words having the words this person used.
    chatrooms contains the chatrooms that this person talked
    '''
    def __init__(self, name):
        self.name = name
        self._words = Words()
        self._curses = Words()
        self.chatrooms = []
        self.curse_cnt = 0

    def __str__(self):
        return self.name

    def add_word(self, word, idx=None, curse=False):
        if curse:
            self._curses.add(word, idx)
            self.curse_cnt += 1
        else:
            self._words.add(word, idx)

    def count_words(self, talkday=None, chatroom=None, sort_by_f=False, curse=False):
        if curse:
            return self._curses.words_count(talkday, self, chatroom, sort_by_f)
        else:
            return self._words.words_count(talkday, self, chatroom, sort_by_f)

    def get_words(self, talkday=None, curse=False):
        ''' It returns dictionary the words and the number person used. '''
        ret = {}
<<<<<<< HEAD
=======

>>>>>>> 912dde648d4895a14e041f1c21e54664e9c40b63
        for word in self._words if not curse else self._curses:
            cnt = word.get_count(talkday=talkday, person=self)
            if cnt:
                ret[word.name] = cnt
        return ret

class People:
    ''' People is a collection of person. '''
    def __init__(self):
        self._people = []

    def __len__(self):
        return len(self._people)

    def __getitem__(self, idx):
        return self._people[idx]

    def __str__(self):
        ret = ""
        for person in self._people:
            ret += str(person) + ", "
        ret = ret[:-2]

        return ret
    
    def append(self, person):
        return self._people.append(person)

    def names(self):
        ''' It returns all people names iterator '''
        for p in self._people:
            yield p.name
        
    def find(self, name):
        ''' find name. if it were, return Person instance else None. '''
        names = list(self.names())
        if name in names:
            return self._people[names.index(name)]
        else:
            return None
