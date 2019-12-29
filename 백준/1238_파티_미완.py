from heapq import heappush, heappop

N, M, X = map(int, input().split())
board = [[] for i in range(N + 1)]

for i in range(M):
    st, ed, t = map(int, input().split())
    board[st].append([t, ed])

spend = [0] * (N+1)

