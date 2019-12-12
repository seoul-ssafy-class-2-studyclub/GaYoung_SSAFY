from collections import deque

N = int(input())
x = 1

q = deque([x])
near = [2 * x, 2 * x + 1]
cnt = 0

while q:
    cnt += 1
    for i in range(len(q)):
        xx = q.popleft()
