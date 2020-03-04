from collections import deque
from pprint import pprint
def isWall(x, y):
    if x < 0 or x > N - 1 :
        return True
    if y < 0 or y > N - 1:
        return True
    return False
def DFS(start_x, start_y):
    global max_count
    global start
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count = 1
    x = start_x
    y = start_y
    while True:
        if max_count < count:
            max_count = count
            start = data[start_x][start_y]
        elif max_count == count:
            if start > data[start_x][start_y]:
                start = data[start_x][start_y]
        for mode in range(4):
            Testx = x + dx[mode]
            Testy = y + dy[mode]
            if isWall(Testx, Testy) == False:
                if data[x][y] + 1 == data[Testx][Testy]:
                    count += 1
                    x = Testx
                    y = Testy
                    break
        else:
            return




TC=int(input())
for test_case in range(1, TC+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    start = 999999999
    max_count = 0
    for i in range(N):
            for j in range(N):
                DFS(i, j)

    print("#{} {} {}".format(test_case, start, max_count))