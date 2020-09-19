def solution(board):
    answer = 0
    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

'''
1. bfs + 로봇은 2칸을 차지한다. + 회전
2. 방문 여부를 비교해야한다. -> 로봇의 좌표를 이용해야한다.
3. 회전함수 = turn -> 회전은 4가지 경우로 할 수 있다.
'''

from collections import deque


def turn():
    near = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    return 0


len_board = len(board)
bd = [[1] * (len_board + 2) for _ in range(len_board + 2)]
for i in range(len_board):
    for j in range(len_board):
        bd[1+i][1+j] = board[i][j]


q = deque([[(1, 1), (1, 2), 0]])
visit = []

while q:
    first, second, cnt = q.popleft()

    if second[0] == len_board and second[1] == len_board:
        print(cnt)
        break

