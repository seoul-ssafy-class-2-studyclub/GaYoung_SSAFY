def solution(n):
    cnt = 1
    start = n // 2 + 1
    for i in range(start, 0, -1):
        total = 0
        for j in range(i, 0, -1):
            total += j
            if total == n:
                cnt += 1
                break
            elif total > n:
                break

    # print(cnt)
    return cnt

n = 15
