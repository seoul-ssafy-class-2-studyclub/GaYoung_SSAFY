'''
최대 16진수이므로 n진수 표현하기.
숫자는 최대 n * t까지 구하면 된다.
이후, 튜브순서만 빼오면 정답
'''

# n, t, m, p = 2, 4, 2, 1
# n, t, m, p = 16, 16, 2, 1
n, t, m, p = 16, 16, 2, 2


def make_n(n, number):  # n진수로 변환
    total = '0123456789ABCDEF'
    i, j = divmod(number,n)
    if i == 0:
        return total[j]
    else:
        return make_n(n, i) + total[j]


def solution(n, t, m, p):
    answer = ''
    number = 0
    while len(answer) < m * t:
        answer += make_n(n, number)
        number += 1

    result = ''
    for i in range(len(answer)):
        if i % m == p - 1:
            result += answer[i]
        if len(result) == t:
            break

    return result
