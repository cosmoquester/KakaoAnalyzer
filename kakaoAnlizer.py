from re import search, compile
from Chatroom import Chatroom
from datetime import datetime

def Analize(data_in):
    '''
    Analize kakaoTalk text. input parameter is file io or string.
    It returns Chatroom instance.
    '''

    # Regular Expressions
    datetime_exp = compile('-+ (?P<year>\d{4})년 (?P<month>\d{1,2})월 (?P<day>\d{1,2})일 .요일 -+\r?\n?')
    message_exp = compile('\[(?P<name>.+?)\] \[(?P<afm>..) (?P<hour>\d{1,2}):(?P<min>\d{2})\] (?P<con>.+)')

    # Variables, queue is for multiline message.
    date = None
    chatname = None
    line = True
    queue = []

    if type(data_in) == str:
        from io import StringIO
        data_in = StringIO(data_in)

    # Find Chatroom Name
    while line and not chatname:
        line = data_in.readline()
        chatname = search('(.*?) 님과 카카오톡 대화', line).group(1)
        chatroom = Chatroom(chatname)

    # Check Text lines
    while line:
        line = data_in.readline()

        # Check line with regular expression
        m_date = datetime_exp.match(line)
        m_message = message_exp.match(line)

        # The case this line is new date.
        if m_date:
            # Excute
            if len(queue):
                chatroom.append(*queue[0])
                del queue[0]
            # Update date
            date = datetime(int(m_date.group('year')), int(m_date.group('month')), int(m_date.group('day')))

        # The case this line is new message.
        elif m_message:
            # Excute
            if len(queue):
                chatroom.append(*queue[0])
                del queue[0]

            name = m_message.group('name')
            afm = m_message.group('afm')
            hour = int(m_message.group('hour'))
            minute = int(m_message.group('min'))
            content = m_message.group('con')

            if afm == '오후' and hour != 12:
                hour += 12
            date = date.replace(hour=hour, minute=minute)

            # Enqueue
            queue.append([date, name, content])

        # The case this line is addition string of last message.
        elif len(queue):
            queue[-1][2] += '\n' + line
    
    # Last Dequeuing
    if len(queue):
        chatroom.append(*queue[0])

    data_in.close()
    return chatroom











if __name__ == '__main__':
    f_name = input("Please input conversation file name without extension(ex conv)\n: ")
    f = open(f_name, 'r', encoding='utf8')

    chatroom = Analize(f)