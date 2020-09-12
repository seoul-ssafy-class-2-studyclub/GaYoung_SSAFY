def solution(n, s, a, b, fares):
    answer = 0
    return answer

# n = 7
# s = 3
# a = 4
# b = 1
# fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

# n = 6
# s = 4
# a = 5
# b = 6
# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

from collections import deque

visit = [0] * (n+1)
visit[s] = 1
q = deque([[s, 0]])
print(q)

muzi = 0
appeach = 0
check = {}

while q:

    x, cost = q.popleft()

    if x == a or x == b:
        break

    for start, end, taxi in fares:
        if start == x and visit[start] == 1:
            q.append([end, cost + taxi])
            visit[end] = 1
        if end == x and visit[end] == 1:
            q.append([start, cost + taxi])
            visit[start] = 1
    print(q)