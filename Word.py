class Word:
    '''
    A Word instance is a word like "apple".
    It has information about who, when, how much use this.
    '''
    def __init__(self, name):
        self.name = name
        self._history = []

    def append(self, talkday, person, chatroom, message):
        self._history.append((talkday, person, chatroom, message))

    def __str__(self):
        return self.name

    def __getitem__(self, idx):
        return self._history[idx]

    def __eq__(self, other):
        if type(other)==Word: other = other.name
        return self.name == other

    def __ne__(self, other):
        if type(other)==Word: other = other.name
        return self.name != other

    def __lt__(self, other):
        if type(other)==Word: other = other.name
        return self.name < other
    
    def __le__(self, other):
        if type(other)==Word: other = other.name
        return self.name <= other

    def __gt__(self, other):
        if type(other)==Word: other = other.name
        return self.name > other
    
    def __ge__(self, other):
        if type(other)==Word: other = other.name
        return self.name >= other
    
    def get(self, talkday=None, person=None, chatroom=None):
        '''
        You can bring Word history using 'get' mothod.
        It returns Messages by iterator according to named parameter person or talkday.
        '''
        for t, p, c, m in self._history:
            if (not talkday or t == talkday) and\
                (not person or p is person) and\
                (not chatroom or c is chatroom):
                yield m
        
    def get_count(self, talkday=None, person=None, chatroom=None):
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

class Words:
    '''
    This is like sorted Lists.
    Maintain sorted for speed.
    '''
    def __init__(self):
        self._words = []

    def __len__(self):
        return len(self._words)

    def __getitem__(self, idx):
        return self._words[idx]

    def names(self):
        for w in self._words:
            yield w
    
    def add(self, word:Word, idx=None):
        ''' Add word instance to this.  '''
        if idx:
            self._words.insert(idx, word)
            return True
        else:
            lower_bound=0
            upper_bound=len(self)
            mid = (lower_bound + upper_bound) // 2
            
            # Binary search
            while lower_bound < upper_bound:
                mid = (lower_bound + upper_bound) // 2
                if self[mid] < word:
                    lower_bound = mid + 1
                elif self[mid] > word:
                    upper_bound = mid
                else:
                    break

            # Duplication
            if mid < len(self) and self[mid] == word:
                return False
            
            else:
                self._words.insert(mid, word)

    def find(self, word, create=False):
        '''
        find and return Word instance if exist.
        When create is True, return new Word instance despite absence.
        word parameter can be string or Word type.
        '''
        lower_bound=0
        upper_bound=len(self)
        mid = (lower_bound + upper_bound) // 2
        
        # Binary search
        while lower_bound < upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if self[mid] < word:
                lower_bound = mid + 1
            elif self[mid] > word:
                upper_bound = mid
            else:
                break

        # Success and return
        if mid < len(self) and self[mid] == word:
            return self[mid]

        # Find fail so create
        else:
            if create:
                if type(word) != Word:
                    new_word = Word(word)
                    self.add(new_word, idx=mid)
                    word = new_word
                return word
            else:
                return False
    
    def words_count(self, talkday=None, person=None, chatroom=None, sort_by_f=False):
        '''
        Return {word:count} dictionary of lists of (word:count) when sort_by_f=true
        You can bring counts according to talkday, person, chatroom.
        '''
        ret = {}
        for word in self._words:
            cnt = word.get_count(talkday, person, chatroom)
            if cnt:
                ret[word.name] = cnt
        if sort_by_f:
            ret = sorted(list(ret.items()), key=lambda x:x[1])
            ret.reverse()
        return ret