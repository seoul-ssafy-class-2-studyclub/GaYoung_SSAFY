N = int(input())
dp = [[100000*N]*(N+1) for _ in range(N+1)]
E = int(input())
for _ in range(E):
    a, b, c = map(int, input().split())
    if dp[a][b] > c:  # 노선이 단순히 하나가 아님
        dp[a][b] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        if i != k:
            for j in range(1, N+1):
                if j != i and j != k:
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(1, N+1):
    result = []
    for j in range(1, N+1):
        if dp[i][j] < 100000*N:
            result.append(dp[i][j])
        else:
            result.append(0)
    print(' '.join(map(str, result)))