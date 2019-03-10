from re import search, compile
from Chatroom import Chatroom
from datetime import datetime

def Analize(data_in, line_num=None):
    '''
    Analize kakaoTalk text. input parameter is file io or string.
    It returns Chatroom instance.
    '''

    # Regular Expressions
    datetime_exp = compile('-+ (?P<year>\d{4})년 (?P<month>\d{1,2})월 (?P<day>\d{1,2})일 .요일 -+\r?\n?')
    message_exp = compile('\[(?P<name>.+?)\] \[(?P<afm>..) (?P<hour>\d{1,2}):(?P<min>\d{2})\] (?P<con>.+)')

    # Variables, queue is for multiline message.
    loop = 0
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

        if line_num:
            loop += 1
            print(loop, '/', line_num)
    
    # Last Dequeuing
    if len(queue):
        chatroom.append(*queue[0])

    data_in.close()
    return chatroom

if __name__ == '__main__':
    linenum = 0
    f_name = input("Please input conversation file name without extension(ex conv)\n:")
    
    if len(f_name) > 4 and f_name[-4:] != '.txt' or len(f_name) <= 4:
        f_name += '.txt'
    
    try:
        f = open(f_name, 'r', encoding='utf8')
        while f.readline(): linenum+=1
        f.close()
        f = open(f_name, 'r', encoding='utf8')

    except:
        f = open(f_name, 'r')
        while f.readline(): linenum+=1
        f.close()
        f = open(f_name, 'r')

    chatroom = Analize(f, linenum)

    while True:
        sel = input('1. Chatroom name\n'+
                '2. Chat Members\n'+
                '3. Message Count\n'+
                '4. Message Rate\n'+
                '5. View a day conversation\n'+
                '6. View a person words by frequency\n'
                '7. Exit\n:')
        
        if sel == '1':
            print(chatroom.name)
        elif sel == '2':
            print(chatroom.people)
        elif sel == '3':
            print("Total:", chatroom.tot_msg)
            print(str(chatroom.tot_person)[1:-1])
        elif sel == '4':
            for n, r in chatroom.tot_person_rate():
                print("{:7} {:3.3}%".format(n, r*100))
        elif sel == '5':
            for i, d in enumerate(chatroom.talkdays):
                print("{}: {}".format(i,d))
            sel = int(input("select the day: "))
            msgs = chatroom.talkdays[sel].get_Msg(chatroom)
            if msgs:
                for i in msgs:
                    print(i)
        elif sel == '6':
            for i, d in enumerate(chatroom.people):
                print("{}: {}".format(i,d))
            sel = int(input("select the person: "))
            person = chatroom.people[sel]
            words_cnts = person.words.words_count(person=person, chatroom=chatroom, sort_by_f=True)

            sel = int(input("How much numbers you want to print: "))
            for i in range(min(sel, words_cnts)):
                print("{}. {} : {} Times".format(i+1, words_cnts[i][0], words_cnts[i][1]))
        elif sel == '7':
            exit()

        else:
            print('Please Select in Menu.')
        print()