def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    l, r = 1, 2
    answer = 0
    for i in range(n-2):
        answer = l+r
        l, r = r, answer

    return answer % 1000000007

print(solution(4))

