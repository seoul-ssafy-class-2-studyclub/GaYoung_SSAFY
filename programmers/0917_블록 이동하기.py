from collections import deque

def solution(board):
    answer = 0
    return answer

board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]

n = len(board)
visit = [[0] * n for _ in range(n)]
q = deque([[[0, 0], [0, 1]]])