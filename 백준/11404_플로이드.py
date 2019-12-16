from pprint import pprint

N = int(input())
M = int(input())

inf = float('inf')
cost = [[inf] * (N+1) for _ in range(N+1)]
for m in range(M):
    start, end, money = map(int, input().split())
    if money < cost[start][end]:
        cost[start][end] = money
'''
cost
[[inf, inf, inf, inf, inf, inf],
 [inf, inf, 2, 3, 1, 10],
 [inf, inf, inf, inf, 2, inf],
 [inf, 8, inf, inf, 1, 1],
 [inf, inf, inf, inf, inf, 3],
 [inf, 7, 4, inf, inf, inf]]
'''

for mid in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            if start != end and cost[start][end] > cost[start][mid] + cost[mid][end]:
                cost[start][end] = cost[start][mid] + cost[mid][end]

for row in cost[1:]:
    for col in row[1:]:
        if col == inf:
            print(0, end=' ')
        else:
            print(col, end=' ')
    print()