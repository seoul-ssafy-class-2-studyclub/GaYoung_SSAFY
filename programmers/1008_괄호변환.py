# p = '(()())()'
# p = ')('
p = '()))((()'

def balance(word):
    cnt = 0
    for i in word:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

    return cnt


def correct(word):
    left, right = 0, 0
    for i in word:
        if i == '(':
            left += 1
        if i == ')':
            right += 1

        if right > left:
            return False

    if right == left:
        return True

    return False


def make_uv(p):
    for i in range(1, len(p)+1):
        if balance(p[:i]) == 0:
            u = p[:i]
            v = p[i:]
            return u, v

def solution(p):

    if p == '':  # 1번
        return ''

    u, v = make_uv(p)  # 2번

    answer = ''
    if correct(u):  # 3번
       return u + solution(v)  # 3-1번

    else:
        answer += '(' + solution(v) + ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

print(solution(p))