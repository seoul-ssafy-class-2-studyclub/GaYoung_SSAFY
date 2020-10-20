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


def pelindrom1(string):

    if string == string[::-1]:
        return [True, len(string)]
    return [False, 0]

def solution1(s):
    mymax = 0
    for i in range(len(s)):
        cnt = 0
        for j in range(len(s), i, -1):
            result = pelindrom1(s[i:j])
            # print(result)
            if result[0]:
                cnt = result[1]
                break

        if mymax < cnt:
            mymax = cnt

    return mymax

print(solution1(s))