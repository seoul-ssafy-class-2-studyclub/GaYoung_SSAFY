'''
[ 입력 ]
1. R(행), C(열), M(상어 수)
2. M개의 줄에 상어의 정보. (r, c): 상어의 위치, s: 속력, d: 이동방향, z: 크기
                                            d=1:위, d=2:아래, d3:오른쪽, 4:왼쪽
'''


'''
[ 문제 이해 ]
1. 상어는 최대 1마리
2. 상어는 크기, 속도 가지고있음.
3. 1초 동안 일어나는 일
    - 낚시왕 오른쪽으로 한칸 이동
    - 땅과 제일 가까운 상어 잡기(잡힌 상어는 사라짐)
    - 상어 이동 : 격자판의 경계 -> 방향 반대, 속력 유지
               : 이동 후 한칸에 상어 2마리 가능 -> 크기 큰 상어가 나머지 다 잡아먹음
'''

# 방법1. board에 칸마다 [s, d, z]넣고 이동하기
#     -> but, person == col일때, 상어를 잡아야하는데 col을 따오기 힘듦
#     -> 그래서 board에 [r, c, s, d, z]넣어서 하나씩 빼면서 확인
# from heapq import heappop, heappush
#
# R, C, M = map(int, input().split())
# sharks = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
#
# for m in range(M):
#     x, y, s, d, z = map(int, input().split())
#     sharks[x][y] = [s, d, z]
#
# # print(sharks)
# total = 0  # 상어 크기의 합
# person = 0
# while True:
#     person += 1
#     if person > C:
#         break
#
#     if len(sharks) == 0:
#         break
#
#     shark_col = []
#
#         # print(sharks)
#         # 같은 줄에 있는 상어 잡기
#         # 잡을 때, 같은 줄에 있는 상어가 있을 때, 하나면 그거 잡으면 됨
#         # but, 여러개라면 그 중에 row가 작은 것을 택해야함
#         if y == person:
#             heappush(shark_col, (x, z))
#             print(shark_col)
#
#     # 잡을 상어가 있다면,
#     # if len(shark_col) != 0:
#     #     pass
#
#     # 잡을 상어가 없다면, 상어 이동



# 방법2. board에 [r, c, s, d, z]넣어서 하나씩 빼면서 확인
from heapq import heappop, heappush
from pprint import pprint

R, C, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(M)]
print(shark)
total = 0  # 상어 크기의 합
person = 0
while True:
    person += 1
    if person > C:  # 사람이 board판을 벗어나면 잡을 수 없음
        break

    if len(sharks) == 0:  # 상어가 한마리도 없으면
        break

    shark_col = []
    for i in range(len(sharks)):
        x, y, s, d, z = sharks[i]
        # 같은 줄에 있는 상어 잡기
        # 잡을 때, 같은 줄에 있는 상어가 있을 때, 하나면 그거 잡으면 됨
        # but, 여러개라면 그 중에 row가 작은 것을 택해야함
        if y == person:
            heappush(shark_col, (x, y, z, i))

    # 잡을 상어가 있다면, total에 더하고, sharks판에서 삭제
    if len(shark_col) != 0:
        catch = heappop(shark_col)  # catch = y가 person이랑 같은 줄에서(shark_col) x가 가장 작은 경우
        sharks.pop(catch[3])
        total += catch[2]  # 상어 크기 더해주기

    # board판에 이동한 상어 넣기
    board = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
    eat = []
    for i in range(len(sharks)):
        x, y, s, d, z = sharks[i]

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

        sharks[i] = (x, y, s, d, z)

        if not board[x][y]:  # 비어있으면
            board[x][y].append([s, d, z, i])
        else:  # 채워져있으면
            if z > board[x][y][2]:  # 새로온 애가 기존애보다 크면
                eat.append(board[x][y][3])
                board[x][y] = [s, d, z, i]
            else: # 새로온 애가 기존애보다 작으면
                eat.append(i)  # 몇번째인지 확인


    # 상어 삭제
    for e in range(len(eat)):
        sharks.pop(eat[e])


    print('person')
    print(person)
    print('board')
    pprint(board)
    print('sharks')
    pprint(sharks)
    print(total)
    print('------------------------------------------------------------------------------')

