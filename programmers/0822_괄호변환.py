def balance(p):  # 균형잡힌 괄호 문자열
    cnt = 0

    for i in p:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True
    return False


def correct(p):  # 올바른 괄호 문자열
    left = 0
    right = 0

    for i in p:
        if i == '(':
            left += 1
        else:
            right += 1

        if right > left:
            return False

    if left == right:
        return True
    else:
        return False

def makeuv(p):
    u = ''
    v = ''
    for i in range(len(p)+1):
        if balance(p[:i+1]):
            u = p[:i+1]
            v = p[i+1:]
            break

    return u, v


def solution(p):

    if p == '':
        return ''
    # 2번
    u, v = makeuv(p)
    # 3번
    if correct(u):
        u += solution(v)
        return u

    # res = ''  # 빈문자열
    else:
        res = '(' + solution(v) + ')'  # 4-1, 4-2, 4-3
        uu = u[1:-1]
        for i in range(len(uu)):
            if uu[i] == '(':
                res += ')'
            else:
                res += '('
        return res


# p = '(()())()'
# p = '(()))('
# p = ')('
p = '()))((()'
print(solution(p))