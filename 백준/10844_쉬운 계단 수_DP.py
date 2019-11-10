'''
45656 -> 인접한 모든 자리수의 차이가 1 -> 계단 수라고 한다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지?(0으로 시작하는 수는 없다.)
'''

'''
ex
N = 1 => 1, 2, 3, 4, 5, 6 ...
N = 2 => 10, 12, 21, 23, 32, 34, 43, 45...
'''

# 길이가 N일 때, 마지막 수가 L일 경우의 계단의 수
# L=0 => dp[N][L] = dp[N-1][L+1]
# L=1~8 => dp[N][L] = dp[N-1][L-1] + dp[N-1][L+1]
# L=9 => dp[N][L] = dp[N-1][L-1]

N = int(input())
dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] += dp[i - 1][j + 1]
        elif 1 <= j <= 8:
            dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]
        elif j == 9:
            dp[i][j] += dp[i - 1][j - 1]

ans = 0
for i in range(10):
    ans += dp[N][i]

print(ans % 1000000000)