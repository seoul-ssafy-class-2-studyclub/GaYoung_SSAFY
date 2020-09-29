# S = 'aabab'
# S = 'dog'
# S = 'aa'
S= 'baaaa'

def solution(S):
    S = S.replace('b', ' ').replace('c', ' ').replace('d', ' ').replace('e', ' ').replace('f', ' ').replace('g', ' ')\
        .replace('h', ' ').replace('i', ' ').replace('j', ' ').replace('k', ' ').replace('l', ' ').replace('m', ' ').\
        replace('n', ' ').replace('o', ' ').replace('p', ' ').replace('q', ' ').replace('r', ' ').replace('s', ' ').\
        replace('t', ' ').replace('u', ' ').replace('v', ' ').replace('w', ' ').replace('x', ' ').replace('y', ' ').replace('z', ' ')

    S = S.split(' ')

    cnt = 0
    for i in range(len(S)):
        if len(S[i]) > 2:
            return -1

        elif len(S[i]) == 2:
            continue

        elif len(S[i]) < 2:
            cnt += 2-len(S[i])

    return cnt

print(solution(S))