board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

n = len(board)
visit = [[[0] * n for _ in range(n)] for _ in range(2)]
# 로봇이 가로, 세로인 경우