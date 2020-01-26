bingo = []
for n in range(5):
    bingo.append(list(map(int, input().split())))

point_list = []
for n in range(5):
    point_list += [int(i) for i in input().split()]

result = 0
line = 0
visit = [0, 0]  # 대각선, 역대각선
for k in range(25):
    if result == 1:
        break
    for x in range(5):
        for y in range(5):
            point = point_list[k]
            if point == bingo[x][y]:
                bingo[x][y] = 0

                # 가로
                if bingo[x] == [0, 0, 0, 0, 0]:
                    line += 1

                # 세로
                flag = True
                for i in range(5):
                    if bingo[i][y] != 0:
                        flag = False
                if flag:
                    line += 1

                # 대각선 -> 1개임 -> print해보면 여러번 반복!
                #        -> 한번 왔던 곳은 가지 않음
                flag = True
                for i in range(5):
                    if bingo[i][i] != 0:
                        flag = False
                if flag and visit[0] == 0:
                    line += 1
                    visit[0] = 1

                # 대각선 역
                flag = True
                for i in range(5):
                    if bingo[i][4 - i] != 0:
                        flag = False
                if flag and visit[1] == 0:
                    line += 1
                    visit[1] = 1

                if line >= 3:
                    result = 1
                    print(k + 1)
