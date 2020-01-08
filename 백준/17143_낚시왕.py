# 칸에는 상어 최대 한마리
# 낚시왕은 0번째에서 출발
# 1초 동안 일어나는 일: 1. 낚시왕 오른쪽으로 한칸 이동
#                     2. 낚시왕이 있는 열에 있는 상어 중 땅과 제일 가까운 상어 잡기.
#                         (잡은 상어는 사라짐)
#                     3. 상어 이동

R, C, M = map(int, input().split())
sharks = {}
for m in range(M):
    sharks[m] = list(map(int, input().split()))

person = 0
total = 0
death = 0
while True:

    person += 1

    if person > C:
        break

    # 모든 상어가 없어지면
    if death == M:
        break

    catch_key = -1
    catch_x = R + 2
    for key, value in sharks.items():
        x, y, s, d, z = value

        if x == -1:
            continue
        # 같은 줄에 있는 상어 잡기
        # 잡을 때, 같은 줄에 있는 상어가 있을 때, 하나면 그거 잡으면 됨
        # but, 여러개라면 그 중에 row가 작은 것을 택해야함
        if y == person:
            if catch_x > x:
                catch_key = key
                catch_x = x
        # 잡을 상어가 있다면, total에 더하고, sharks판에서 삭제
    if catch_key >= 0:
        total += sharks[catch_key][4]
        sharks[catch_key] = [-1, -1, -1, -1, -1]
        death += 1

    # board: 이동한 상어들을 넣어서 비어있으면 넣고, 안비어있으면 비교하기 위해
    board = [[[] for _ in range(C + 1)] for _ in range(R + 1)]

    for key, value in sharks.items():
        x, y, s, d, z = value

        if x == -1:
            continue
        # 방법1. 범위 하나하나 분리 -> s가 10이고, R이 4면 여러번 굴러야함
        # 이때, x가 -1이면 방향 바꾸고, x가 -5이면 방향 유지
        move_r = s % (2 * R - 2)
        move_c = s % (2 * C - 2)
        if d == 1:  # x좌표만 이동
            xx = x - move_r
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
            xx = x + move_r
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
            yy = y + move_c
            if yy > C:  # 칸을 벗어났을 때
                y = 2 * C - yy
                if y < 1:  # 이때는 방향 유지
                    y = 2 - y
                else:  # x < R이면 2, 3, 4로 증가하는 부분이므로
                    d = 4
            else:
                y = yy

        else:  # y축만 이동
            yy = y - move_c
            if yy < 1:
                y = 2 - yy
                if y > C:
                    y = 2 * C - y
                else:
                    d = 3
            else:
                y = yy

        eat = []
        if len(board[x][y]) == 0:  # board판 비어있는거
            board[x][y].extend([key, s, d, z])
            sharks[key] = x, y, s, d, z
        else:  # board판에 상어가 있다면
            if z > board[x][y][3]:
                eat.append(board[x][y][0])
                board[x][y] = [key, s, d, z]
                sharks[key] = x, y, s, d, z
            else:
                eat.append(key)

        if eat:
            for e in eat:
                sharks[e] = [-1, -1, -1, -1, -1]
                death += 1


    print('board')
    print(board)
    print('sharks')
    print(sharks)
    print(total)
    print('-------------------------------------------')

