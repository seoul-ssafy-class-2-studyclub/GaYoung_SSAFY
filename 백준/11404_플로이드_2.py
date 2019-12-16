N = int(input())

dp = [[1e9]*(N+1) for _ in range(N+1)]

E = int(input())

for _ in range(E):
    a, b, c = map(int, input().split())
    if dp[a][b] > c:  # 노선이 단순히 하나가 아님
        dp[a][b] = c  # 최소거리로 갱신해줌

# dp[x][x]면 값을 바꾸지 않음 -> i != k와 같은 조건문 작성
for k in range(1, N+1):
    for i in range(1, N+1):
        if i != k:
            for j in range(1, N+1):
                if j != i and j != k:
                    # k는 경유지이므로 dp[i][k]+dp[k][j] 이런 식이 나올 수 있음
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(1, N+1):
    result = []
    for j in range(1, N+1):
        if dp[i][j] < 100000*N:
            result.append(dp[i][j])
        else:
            result.append(0)
    print(' '.join(map(str, result)))