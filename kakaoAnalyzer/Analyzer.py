from re import search, compile
from datetime import datetime
from .msgstruct import *


def Analyze(data_in, line_num=None, line_analyze=None, mode=None):
    '''
    Analyze kakaoTalk text. input parameter is file io or string.
    It returns Chatroom instance.
    '''

    # Variables, queue is for multiline message.
    loop = 0
    date = None
    chatname = None
    line = True
    queue = []

    if type(data_in) == str:
        from io import StringIO
        data_in = StringIO(data_in)

    # Select Mode
    if mode:
        if mode in ('android', 1):
            mode = 1 # 1 is Android
        elif mode in ('winpc', 'win', 2):
            mode = 2 # 2 is Windows PC
        elif mode in ('ios', 'ipad', 3):
            mode = 3 # 3 is iOS
        else:
            mode = None

    # Find Chatroom Name
    line = data_in.readline()
    chatname = search('(.+?) 님과 카카오톡 대화|(.+?) \d+ 카카오톡 대화', line)

    # Set Chatname
    if chatname:
        chatname = chatname.group(1,2)
        chatname = chatname[0] if chatname[0] else chatname[1]
    else:
        chatname = line

    # Android
    if mode == 1:
        chatname = chatname[1]
        datetime_exp = compile('(?P<year>\d{4})년 (?P<month>\d{1,2})월 (?P<day>\d{1,2})일 .. \d{1,2}:\d{2}\r?\n?$')
        message_exp = compile('\d{4}년 \d{1,2}월 \d{1,2}일 (?P<afm>..) (?P<hour>\d{1,2}):(?P<min>\d{2}), (?P<name>.+?) : (?P<con>.+)')
        etc_exp = compile('\d{4}년 \d{1,2}월 \d{1,2}일 .. \d{1,2}:\d{1,2}, .+')

    # Windows PC
    elif mode == 2:
        chatname = chatname[0]
        datetime_exp = compile('-+ (?P<year>\d{4})년 (?P<month>\d{1,2})월 (?P<day>\d{1,2})일 .요일 -+\r?\n?')
        message_exp = compile('\[(?P<name>.+?)\] \[(?P<afm>..) (?P<hour>\d{1,2}):(?P<min>\d{2})\] (?P<con>.+)')
        etc_exp = compile('.+님이 나갔습니다.\r?\n?|.+님이 .+님을 초대하였습니다.\r?\n?|.+님이 들어왔습니다.\r?\n?')

    # ipad
    elif mode == 3:
        chatname = line
        datetime_exp = compile('(?P<year>\d{4})년 (?P<month>\d{1,2})월 (?P<day>\d{1,2})일 .요일\r?\n?')
        message_exp = compile('(?P<year>\d{4}). (?P<month>\d{1,2}). (?P<day>\d{1,2}). (?P<afm>..) (?P<hour>\d{1,2}):(?P<min>\d{1,2}), (?P<name>.+?) : (?P<con>.+?)\r?\n?$')
        etc_exp = compile('\d{4}. \d{1,2}. \d{1,2}. .. \d{1,2}:\d{1,2}: .+')
    chatroom = Chatroom(chatname, line_analyze)

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
        elif len(queue) and not etc_exp.match(line):
            queue[-1][2] += '\n' + line

        if line_num:
            loop += 1
            print(loop, '/', line_num)
    
    # Last Dequeuing
    if len(queue):
        chatroom.append(*queue[0])

    data_in.close()
    return chatroom
