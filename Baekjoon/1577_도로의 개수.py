from pprint import pprint

N, M = map(int, input().split())
K = int(input())
board = [[0] * M for _ in range(N)]

for k in range(K):
    a, b, c, d = map(int, input().split())


pprint(board)