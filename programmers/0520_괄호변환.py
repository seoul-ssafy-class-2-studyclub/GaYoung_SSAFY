
# p = '(())()'
# p = '(()))('
# p = ')('
p = '()))((()'

def balance(p):
    cnt = 0
    # len(p)가 홀수이면 무조건 balance아님
    if len(p) % 2 != 0:
        return False

    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0:
        return True
    return False

def correct(p):
    r = 0
    l = 0
    for i in p:
        if i == '(':
            l += 1
        else:
            r += 1
        # ()이 모양이 한세트이기 때문에 r이 l보다 클 수 없음
        if r > l:
            return False
    if r == l:
        return True
    else:
        return False

def makeuv(p):
    u = ''
    v = ''
    for i in range(len(p)):
        if balance(p[:i + 1]):
            u = p[:i + 1]
            v = p[i + 1:]
            break
    return u,v

def again(p):
    # 1번
    if p == '':
        return ''

    # 2번, 3번
    res = ''
    u, v = makeuv(p)
    if correct(u):
        u += again(v)  # 3-1번 진행 후 반환필요
        return u

    else:  # 4번
        res += '(' + again(v) + ')'  # 4-1, 4-2, 4-3
        u_remove = u[1:-1]
        for k in range(len(u_remove)):
            if u_remove[k] == '(':
                res += ')'
            else:
                res += '('
    return res
#
def solution(p):
    ans = ''
    if correct(p):
        return p
    else:
        ans += again(p)  # 재귀함수
    return ans

print(solution(p))