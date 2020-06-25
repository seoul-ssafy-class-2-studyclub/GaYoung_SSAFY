'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
'''
# p = '(()())()'
# p = ')('
p = '()))((()'
# p = '))((()'

# 균형잡힌 괄호 문자열
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

# 올바른 괄호문자열
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
    else:
        return False

def makeuv(p):
    u = ''
    v = ''
    for i in range(len(p)):
        if balance(p[:i+1]):
            u += p[:i+1]
            v += p[i+1:]
            break
    return u, v

def problem(p):
    # 1번
    if p == '':
        return ''

    # 2번
    u, v = makeuv(p)  # u=(()()) v=)(

    # 3번
    temp = ''
    if correct(u):  # 3-1에서 시간 많이 걸림,,
        u += problem(v)
        return u

    # 4번
    else:
        # temp += '(' + problem(v) + ')' + u[1:-1][::-1]
        temp += '(' + problem(v) + ')'  # ')' -> '(' 와 '(' -> ')' 로 변환하라는 뜻
        uu = u[1:-1]
        for i in uu:
            if i == '(':
                temp += ')'
            else:
                temp += '('
        '''
        p = "()))((()" 일때, temp = (())()로 잘 나오는데,
        맨 처음 기존의 u+temp가 되어야 정답인데
        '''
        print('temp')
        print(temp)
        return temp

def solution(p):
    if correct(p):
        return p
    else:
        res = problem(p)
        return res

print('solution')
print(solution(p))

