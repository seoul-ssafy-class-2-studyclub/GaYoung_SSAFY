def solution(n):
    ans = [0]
    for i in range(1, n):
        ans = ans + [0] + [(i + 1) % 2 for i in reversed(ans)]

    return ans
