n = 9

def solution(n):
    answer = ''

    while n:

        n, na = divmod(n, 3)

        if na == 0:
            answer = '4' + answer
            n -= 1

        elif na == 1:
            answer = '1' + answer

        elif na == 2:
            answer = '2' + answer

    return answer

print(solution(n))