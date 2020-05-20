# def solution(p):
#     answer = ''
#     return answer



p = '(())()'
# p = '(()))('
# p = ')('
# p = '()))((()'

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

