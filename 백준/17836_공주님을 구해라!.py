'''
6 6 16
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0
'''

from collections import deque
from pprint import pprint
N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q = [(0, 0)]
board[0][0] = 1
time = 0

time_gram = 0
result = 9999999999
gram = False
flag = False
while q:
    time += 1
    # print(time, T)
    if time > T:
        # print('-------------------')
        break
        # flag ==False -> fail

    for i in range(len(q)):
        x, y = q.pop(0)
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < N and 0 <= yi < M:
                if xi == N - 1 and yi == M - 1:
                    result = time
                    # 공주 만나면 stop
                    flag = True
                    break

                elif board[xi][yi] == 0:
                    # visit을 1로 표현
                    board[xi][yi] = 1
                    q.append((xi, yi))

                    # pprint(board)
                    # print(time)
                    # print(flag)
                    # print('===========================')

                elif gram == False and board[xi][yi] == 2:
                    if time + abs(xi - N + 1) + abs(yi - M + 1) <= T:
                        time_gram = time + abs(xi - N + 1) + abs(yi - M + 1)
                        gram = True
                        # print(time)   # 10
        if flag:
            break

    if flag:
        break


if flag == False and gram == False:
    print('Fail')
elif flag and gram:
    if time_gram != 0 and result >= time_gram:
        result = time_gram
    print(result)
elif flag == False and gram == True:
    print(time_gram)
elif flag and gram == False:
    print(result)

'''
5 5 100
0 0 0 0 0
0 0 1 1 1
0 0 1 0 2
0 0 1 1 1
0 0 0 1 0
'''

'''
2 2 1
0 2
0 0
'''