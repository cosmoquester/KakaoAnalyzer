from kakaoAnalyzer import Analyze

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

chatroom = Analyze(f, linenum)

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
        words_cnts = person.count_words(chatroom=chatroom, sort_by_f=True)

        sel = int(input("How much numbers you want to print: "))
        for i in range(min(sel, len(words_cnts))):
            print("{}. {} : {} Times".format(i+1, words_cnts[i][0], words_cnts[i][1]))

    elif sel == '7':
        exit()

    else:
        print('Please Select in Menu.')
    print()