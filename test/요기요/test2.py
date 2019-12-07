def solution(S):
    ls = []
    S = list(S)
    for ss in S:
        if ss != '-' and ss != ' ':
            ls.append(ss)

    result = ''
    for l in range(len(ls)):
        if l % 3 == 2:
            result += ls[l]
            result += '-'
        else:
            result += ls[l]

    result = list(result)
    
    if result[-1] == '-':
        result[-1] = ''

    if result[-2] == '-':
        result[-2] = result[-3]
        result[-3] = '-'
    result = ''.join(result)

    return result
