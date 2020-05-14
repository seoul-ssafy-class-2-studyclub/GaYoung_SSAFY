def solution(N):
    ans = 0
    while N:
        num = N % 2
        if num == 1:  # 점프
            ans += 1
            N -= 1
        else:
            N = N // 2

    return ans
