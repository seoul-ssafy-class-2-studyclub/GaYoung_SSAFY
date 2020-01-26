bingo = []
for n in range(5):
    bingo.append(list(map(int, input().split())))

point_list = []
for n in range(5):
    point_list += [int(i) for i in input().split()]

result = 0
a = []
line = 0
visit = [0, 0]
for k in range(25):
    if result == 1:
        break
    for x in range(5):
        # if result == 1 :
        #     break
        for y in range(5):
            # if result == 1 :
            #     break
            point = point_list[k]
            if point == bingo[x][y]:
                bingo[x][y] = 0
                
                # 가로 빙고
                if bingo[x] == [0, 0, 0, 0, 0]:
                    
                    # print('가로빙고')
                    # print('k = {}'.format(k))
                    # print('x = {}'.format(x))
                    line += 1

                # 세로 빙고
                flag = True
                for i in range(5):
                    if bingo[i][y] != 0:
                        flag = False
                if flag:
                    # print('세로빙고')
                    # print('k = {}'.format(k))
                    # print('y = {}'.format(y))                    
                    line += 1

                # 대각선 x = y
                flag = True
                for i in range(5):
                    if bingo[i][i] != 0:
                        flag = False
                if flag and visit[0] == 0:
                    # print('대각선빙고')
                    # print('k = {}'.format(k))
                    line += 1
                    visit[0] = 1
                
                # 대각선 역방향
                flag = True
                for i in range(5):
                    if bingo[i][4-i] != 0:
                        flag = False
                if flag and visit[1] == 0:
                    # print('대각선역빙고')
                    # print('k = {}'.format(k))
                    line += 1
                    visit[1] = 1
                    
                if line >= 3:
                    result = 1
                    print(k + 1)
