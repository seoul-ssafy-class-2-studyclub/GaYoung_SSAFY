# 방법2. board에 [r, c, s, d, z]넣어서 하나씩 빼면서 확인
from heapq import heappop, heappush
from pprint import pprint
R, C, M = map(int, input().split())
sharks = {}
# 하다보니 sharks랑 board랑 다르게 이동함!
# 그래서 dictionary로 만들어서 key를 기준으로 삭제할거 삭제하고, 이동할거 이동시킴
for i in range(M):
    sharks[i] = list(map(int, input().split()))
# print(sharks)
total = 0  # 상어 크기의 합
person = 0
while True:
    person += 1
    if person > C:  # 사람이 board판을 벗어나면 잡을 수 없음
        break
    if len(sharks) == 0:  # 상어가 한마리도 없으면
        break
    shark_col = []
    for key, value in sharks.items():
        x, y, s, d, z = value
        # 같은 줄에 있는 상어 잡기
        # 잡을 때, 같은 줄에 있는 상어가 있을 때, 하나면 그거 잡으면 됨
        # but, 여러개라면 그 중에 row가 작은 것을 택해야함
        if y == person:
            heappush(shark_col, [key, x, y, z])
    # 잡을 상어가 있다면, total에 더하고, sharks판에서 삭제
    if len(shark_col) != 0:
        catch = heappop(shark_col)  # catch = y가 person이랑 같은 줄에서(shark_col) x가 가장 작은 경우
        # print(catch)
        sharks.pop(catch[0])
        total += catch[3]  # 상어 크기 더해주기
    board = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
    for key, value in sharks.items():
        x, y, s, d, z = value

        if x == -1:
            continue
        # 방법1. 범위 하나하나 분리 -> s가 10이고, R이 4면 여러번 굴러야함
        # 이때, x가 -1이면 방향 바꾸고, x가 -5이면 방향 유지
        if d == 1:  # x좌표만 이동
            move = s % (2 * R - 2)
            xx = x - move
            if xx < 1:  # 칸을 벗어났을 때
                # 상어위치[3, 5, 2, 1, 2]
                # xx = 0 -> 2, -1 -> 3, -2 -> 4, -3 -> 3(원래는 5), -4 -> 2
                x = 2 - xx
                if x > R:  # 이때는 방향 유지
                    x = 2 * R - x
                else:  # x < R이면 2, 3, 4로 증가하는 부분이므로
                    d = 2
            else:
                x = xx
        elif d == 2:  # x축만 이동
            move = s % (2 * R - 2)
            xx = x + move
            if xx > R:  # 칸을 벗어났을 때
                # 상어위치[1, 3, 5, 2, 9]
                # xx = 1 -> 2, 2 -> 3, 3 -> 4 /방향유지/
                #      4 -> 3(원래는5), 5 -> 2(원래는 6), 6 -> 1(원래는 7) /방향변화/
                #      7 -> 2(원래는 8), 8 -> 3(원래는9),,, /방향유지/
                x = 2 * R - xx
                if x < 1:  # 이때는 방향 유지
                    x = 2 - x
                else:  # x < R이면 2, 3, 4로 증가하는 부분이므로
                    d = 1
            else:
                x = xx
        elif d == 3:  # y축만 이동
            move = s % (2 * C - 2)
            yy = y + move
            if yy > C:  # 칸을 벗어났을 때
                y = 2 * C - yy
                if y < 1:  # 이때는 방향 유지
                    y = 2 - y
                else:  # x < R이면 2, 3, 4로 증가하는 부분이므로
                    d = 4
            else:
                y = yy
        else:  # y축만 이동
            move = s % (2 * C - 2)
            yy = y - move
            if yy < 1:
                y = 2 - yy
                if y > C:
                    y = 2 * C - y
                else:
                    d = 3
            else:
                y = yy
        eat = []
        if not board[x][y]:  # 비어있으면
            board[x][y].append([key, s, d, z])
            sharks[key] = x, y, s, d, z
        else:  # 채워져있으면
            if z > board[x][y][0][3]:  # 새로온 애가 기존애보다 크면
                eat += [board[x][y][0][0]]
                board[x][y] = [key, s, d, z]
                sharks[key] = x, y, s, d, z
            else:  # 새로온 애가 기존애보다 작으면
                eat += [key]  # 몇번째인지 확인
    # print('board')
    # pprint(board)
    # print('eat')
    # print(eat)
    # print('--------------------------')
        # 상어 삭제
        for e in eat:
            sharks[e][0] = -1
    print('person')
    print(person)
    print('board')
    pprint(board)
    print('sharks')
    pprint(sharks)
    print(total)
    print('------------------------------------------------------------------------------')
