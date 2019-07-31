# for t in range(int(input())):
n = int(input())
board = []
for i in range(n):  # 보드만들기
    board.append(list(input().split()))
# print(board)
for k in range(len(board)):
    for j in range(len(board)):
        print(board[k][j])