def solution (arrangement):
    answer = 0
    cnt = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':  # 여는괄호 시작이면 check하기 위해서 넣기
            cnt += 1
        elif arrangement[i] == ')':  # 닫는괄호 나타나면 레이저 or 파이프의 끝
            cnt -= 1
            if arrangement[i - 1] == '(':  # 레이저이면 그 전에있는 (들의 갯수 더하기
                answer += cnt
            elif arrangement[i - 1] == ')':  # 막대 마무리
                answer += 1
    # print(answer)

    return answer

'''
닫는 괄호가 나타나면 그 전값이랑 비교해서 레이저인지, 파이프의 끝인지 확인
구분방법 : 닫는괄호 나타나면 바로 전 문자 체크해서 여는괄호면 


'''

# arrangement = '((()())(())())'
# arrangement = '((()()))'
arrangement = '()(((()())(())()))(())'
answer = 0
check = []
cnt = 0
for i in range(len(arrangement)):
    if arrangement[i] == '(':  # 여는괄호 시작이면 check하기 위해서 넣기
        # if arrangement[i+1] == ')':
        #     continue
        cnt += 1
        # check.append((i, arrangement[i]))
    elif arrangement[i] == ')':  # 닫는괄호 나타나면 레이저 or 파이프의 끝
        cnt -= 1
        if arrangement[i-1] == '(': # 레이저이면 그 전에있는 (들의 갯수 더하기
            answer += cnt
            # check.pop()
        elif arrangement[i-1] == ')':  # 막대 마무리
            answer += 1
            # check = []

        print(answer)
        # print(check)
        print('--------------')


print(answer)
