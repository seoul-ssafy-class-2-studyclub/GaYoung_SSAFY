def balance(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True

    return False


def correct(p):
    left = 0
    right = 0
    for i in p:
        if i == '(':
            left += 1
        else:
            right += 1

        if right > left:
            return False

    if right == left:
        return True

    return False

def solution(p):
    if p == '':   # 1번
        return ''

    u, v = '', ''
    for i in range(len(p)):  # 2번
        if balance(p[:i + 1]):
            u += p[:i + 1]
            v += p[i + 1:]
            break

    temp = ''
    if correct(u):  # 3번
        u += solution(v)
        return u

    else:  # 4번
        temp += '(' + solution(v) + ')'
        u = u[1: -1]
        for i in u:
            if i == '(':
                temp += ')'
            else:
                temp += '('

    return temp


# p = "(()())()"
# p = ')('
p = "()))((()"
print(solution(p))
