def solution(n):
    answer = ''
    while n:
        n, na = divmod(n, 3)

        if na == 1:
            answer = '1' + answer
        if na == 2:
            answer = '2' + answer
        if na == 0:
            answer = '4' + answer
            n -= 1

    return answer

n = 10