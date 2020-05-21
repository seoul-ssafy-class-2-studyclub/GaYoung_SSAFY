import pprint

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# 90도씩 도는 것
def rotate(key):
    m = len(key)
    bd = [i[:] for i in key]

    for i in range(m):
        for j in range(m):
            bd[j][m-1-i] = key[i][j]
    return bd

'''
lock을 가운데 두고 (0,0)부터 key를 가지고 한칸씩 이동하면서 채울수있는지 확인
채우지 못했다면 90도 돌려서 다시 (0,0)부터 확인
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 0, 0]
[0, 0, 1, 1, 0, 0, 0]
[0, 0, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
'''
n = len(lock)
m = len(key)
board = [[0]*(n+2*(m-1)) for i in range((n+2*(m-1)))]
for i in range(n):
    for j in range(n):
        board[i + m - 1][j + m - 1] = lock[i][j]
pprint.pprint(board)

# lock의 범위 : start = m-1, end = x + n
# start = m-1
# end = start+n
# for i in range(m):
#     for j in range(m):
#         board[start]

