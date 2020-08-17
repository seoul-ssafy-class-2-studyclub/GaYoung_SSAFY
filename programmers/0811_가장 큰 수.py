def solution(numbers):
    numbers = list(map(str, numbers))

    check = []

    if ''.join(numbers) == '0' * len(numbers):
        # print('yes')
        return '0'

    for number in numbers:
        if len(number) == 4:
            check.append((number, number * 3))

        elif len(number) == 3:
            check.append((number, number * 4))

        elif len(number) == 2:
            check.append((number, number * 6))

        elif len(number) == 1:
            check.append((number, number * 12))

    temp = sorted(check, key=lambda x: x[1], reverse=True)

    answer = ''
    for t in temp:
        answer += t[0]

    return answer


numbers = [3, 30, 31, 0]

# (3, 3333333333), (30, 303030303030), (31, 313131313131), (0, 00000000000000)
# 3, 31, 30 -> 331300

numbers = [0, 0, 0, 0] # => 0000 -> 0
print(solution(numbers))

'''
** 문제점 : numbers = [2, 20, 220]일 때, 2와 20이 동일하게 나온다.
    if len(number) == 4:
        num = number + '0' * 1
        check.append((number, num))
   -> 2, 20, 220이면 2 > 220 > 20 순서로 나와야함
   
** 해결책
222222, 202020, 220220 -> 2 > 220 > 20순서로 나온다
'''

'''
** 문제점 : 0000이 아니라 0으로 나와야한다.
    
** 해결책
    if ''.join(numbers) == '0' * len(numbers):
        print('yes')
        return '0'
        
    이 조건을 추가한다.

'''