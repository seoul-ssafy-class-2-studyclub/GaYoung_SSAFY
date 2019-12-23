from heapq import heappop, heappush

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

seats = []
people = []

for i in range(R):
    for j in range(C):
        if board[i][j] == '.':
            continue
        elif board[i][j] == 'L':
            seats.append((i, j))
        else:
            people.append((i, j))

q = {}
inf = float('inf')

for s1, s2 in seats:
    for p1, p2 in people:
        heappush(q, (((s1 - p1) ** 2 + (s2 - p2) ** 2), (s1, s2), (p1, p2)))

print(q)