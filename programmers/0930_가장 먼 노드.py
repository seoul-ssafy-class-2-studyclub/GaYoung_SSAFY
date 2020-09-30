def solution(n, edge):
    answer = 0
    return answer

from collections import deque

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

check = {i:[] for i in range(1, n+1)}
for a, b in edge:
    check[a].append(b)
    check[b].append(a)

visit = [0] * (n+1)
q = deque([1])
visit[1] = 1
mymax = 0
while q:
    x = q.popleft()

    for j in check[x]:
        if not visit[j]:
            q.append(j)
            visit[j] = visit[x] + 1
            mymax = visit[j]

print(visit.count(mymax))