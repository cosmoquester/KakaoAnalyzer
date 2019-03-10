from datetime import date
from Message import Msgs

class TalkDay(date):
    '''
    The main usage of TalkDay class is providing date.
    Also, it has the messages of the day.
    '''
    def __new__(cls, *args, **kwargs):
        return date.__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        self.Msgss = []

    def get_chatrooms(self):
        return [x.chatroom for x in self.Msgss]

    def append(self, chatroom, msg):

        idx = None
        crs = self.get_chatrooms()
        if chatroom not in crs:
            new_msgs = Msgs(chatroom, self)
            self.Msgss.append(new_msgs)
            idx = -1
        else:
            idx = crs.index(chatroom)

        self.Msgss[idx].append(msg)
    
    def __getitem__(self, idx):
        return self.Msgss[idx]

    def __eq__(self, other):
        return super().__eq__(other)
