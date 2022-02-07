import string
import wordlist
from enum import Enum, IntEnum


class InputState(IntEnum):
    GREY = 1
    YELLOW = 2
    GREEN = 3
    EXIT = 4


allwords = wordlist.La+wordlist.Ta
notin = string
have = string


def count(li):
    countdict = {}
    for word in li:
        for c in word:
            if c in have:
                continue
            if countdict.get(c) is None:
                countdict[c] = 0
            countdict[c] += 1
    return sorted(countdict.items(), key=lambda x: x[1], reverse=True)


def suggest(li):
    countdict = count(li)
    findingword = allwords
    for c in countdict[:min(5, len(countdict))]:
        print(c[0])
        findingword = list(filter(lambda x: c[0] in x, findingword))
        newli = list(filter(lambda x: c[0] in x, li))
        li = newli if len(newli) > 0 else li

    print('finding more info:', findingword)
    print('for answer:', li[:min(5, len(li))])


def grayhandler(li, char):
    notin += char
    return list(filter(lambda x: char not in x, li))


def yellowhandler(li, char, index):
    have += char
    return list(filter(lambda x: char in x and x[index] != char, li))


def greenhandler(li, char, index):
    have += char
    return list(filter(lambda x: x[index] == char, li))


if __name__ == '__main__':
    li = wordlist.La+wordlist.Ta
    while(True):
        print(li)
        suggest(li)
        inp = input(
            ' 1:none\n 2:wrong order\n 3:match\n 4:exit\n other:skip\n>')[0]
        if not inp.isnumeric():
            continue
        elif int(inp) == int(InputState.GREY):
            inp = input('input list of char:')
            for char in inp:
                li = grayhandler(li, char)
        elif int(inp) == int(InputState.YELLOW):
            li = yellowhandler(li, input('input char:'),
                               int(input('input index:')))
        elif int(inp) == int(InputState.GREEN):
            li = greenhandler(li, input('input char:'),
                              int(input('input index:')))
        elif int(inp) == int(InputState.EXIT):
            print('exit')
            break


# ans = list(filter(lambda x: x[-1] == 'r' and x[-2]
#            == 'e' and x[1] == 'l', ans))
# for i in 'tioasfcvbn':
#     ans = list(filter(lambda x: i not in x, ans))
#     # print(ans)
# print(ans)
