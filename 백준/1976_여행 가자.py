N = int(input())
M = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
cities = list(map(int, input().split()))
visit = [False] * N

start = cities[0] - 1
q = [start]
visit[start] = True

while q:
    city = q.pop(0)
    for n in range(N):
        if visit[n] == False and adj[city][n] == 1:
            visit[n] = True
            q.append(n)
        # print('q')
        # print(q)
        # print('visit')
        # print(visit)
        # print('-----------------------------------------')

can = True

for c in cities:
    if not visit[c - 1]:
        can = False
        break

if can:
    result = 'YES'
else:
    result = 'NO'

print(result)
'''
3
3
0 1 0
1 0 1
0 1 0
1 2 3
YES

5
5
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
5 3 2 3 4
YES

3
2
0 0 0
0 0 0
0 0 0
1 1
NO
'''
