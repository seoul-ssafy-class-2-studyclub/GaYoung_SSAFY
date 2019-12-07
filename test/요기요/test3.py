'''
abacdec
dddd
world
cycle
'''

def solution(S):
    cnt = 1
    result = ''
    for s in S:
        if s not in result:
            result += s
        else:
            result = s
            cnt += 1

    return cnt
