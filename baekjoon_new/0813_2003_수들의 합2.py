'''
[투 포인터 문제]
'''

N, M = map(int, input().split())
ls = list(map(int, input().split()))
end = 0
sum = 0
cnt = 0

for start in range(N):
    while sum < M and end < N:
        sum += ls[end]
        end += 1

    if sum == M:
        cnt += 1

    sum -= ls[start]

print(cnt)
