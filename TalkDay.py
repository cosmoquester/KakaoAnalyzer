from datetime import date

'''
The main usage of TalkDay class is providing date.
Also, it has the messages of the day.
'''
class TalkDay(date):

    def __new__(cls, *args, **kwargs):
        return date.__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        self.Msgss = []

    def append(self, msgs):
        self.Msgss.append(msgs)
    
    def __getitem__(self, idx):
        return self.Msgss[idx]

    def __eq__(self, other):
        return super().__eq__(other)
