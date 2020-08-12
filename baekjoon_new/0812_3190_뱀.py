'''
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
'''

'''
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''

'''
6
3
3 4
2 5
5 3
1
3 D
'''
from collections import deque

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

for k in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1  # 사과1, 뱀2, 빈칸0

L = int(input())
change = {}
# 리스트가 아닌 dict로 하는 이유
# dict로 하면 밑에서 시간에 해당할 때 time이 change에 해당하는게 있다면 change_move함수를 써야하는데 이것을 관리하기가 힘들다.
# popleft해버리면 시간이 너무 더 쓰일것같고..
for l in range(L):
    time, dir = input().split()
    change[int(time)] = dir

near = (0, 1)
def change_move(near, direction):
    nx, ny = near
    if nx == 0:
        if direction == 'D':
            if ny > 0:
                return (1, 0)
            else:
                return (-1, 0)

        else:
            if ny > 0:
                return (-1, 0)
            else:
                return (1, 0)

    elif ny == 0:
        if direction == 'D':
            if nx > 0:
                return (0, -1)
            else:
                return (0, 1)

        else:
            if nx > 0:
                return (0, 1)
            else:
                return (0, -1)


time = 0
q = deque([[0, 0]])
board[0][0] = 2
x, y = 0, 0
# while q하면 이게 하나씩 움직이는게 아니라
# 뱀 길이가 2이상일 때 밖으로 하나라도 나가면 stop이 되어야하므로 while True:
while True:
    time += 1

    xi, yi = x + near[0], y + near[1]

    if 0 <= xi < N and 0 <= yi < N:

        # 사과O
        if board[xi][yi] == 1:
            board[xi][yi] = 2
            q.append([xi, yi])

        # 사과X -> 뱀이 지나가면 됨
        elif board[xi][yi] == 0:
            board[xi][yi] = 2
            q.append([xi, yi])
            # 꼬리를 빈칸으로 바꿔야한다. -> board[x][y]하면 바로 전 값이 변하는것이므로
            # 내가 위에서 append했기 때문에 뱀의 머리가 마지막, 꼬리가 앞에 있는것 -> popleft해야함
            nx, ny = q.popleft()
            board[nx][ny] = 0

        # 자기 몸에 부딛히면
        elif board[xi][yi] == 2:
            break

        # x, y를 xi, yi로 갱신해줘야함
        # why? 나는 q에서 pop해서 x,y를 가지고온게 아니라 x, y = 0, 0이라고 지정해주었기 때문!
        x, y = xi, yi

        # 방향 바뀔때
        if time in change:
            # print(time)
            near = change_move(near, change[time])


    else:  # board벗어나면 stop!
        break

    # print('time')
    # print(time)
    # print('q')
    # print(q)
    # print('board')
    # pprint(board)
    # pprint('------------------------------------------------------')

    # print(board)
print(time)

