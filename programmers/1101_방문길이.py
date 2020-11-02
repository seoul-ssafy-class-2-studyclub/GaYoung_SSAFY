def solution(dirs):
    near = {'U':[0, 1], 'R':[1, 0], 'D':[0, -1], 'L':[-1, 0]}
    check = set()
    start_x, start_y = (0, 0)

    for i in dirs:  # 출발지점과 도착지점이 반대여도 같은 간선
        x, y = start_x + near[i][0], start_y + near[i][1]
        if -5 <= x <= 5 and -5 <= y <= 5:
            check.add((start_x, start_y, x, y))
            check.add((x, y, start_x, start_y))
            start_x, start_y = x, y

                # print(start)
                # print('-------------------------------------')

    # print(len(check))
    return len(check) // 2
    

dirs = 'ULURRDLLU'
# dirs = 'LULLLLLLU'

