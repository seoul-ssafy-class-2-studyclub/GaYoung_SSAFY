# s = 'abcdcba'
# s = 'abacde'
# s = 'a'
s = 'abcdefe'

def pelindrom(string):

    if string == string[::-1]:
        return len(string)

def solution(s):
    mymax = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            cnt = pelindrom(s[i:j])

            if cnt != None:
                if mymax < cnt:
                    mymax = cnt

    # print(mymax)
    return mymax
