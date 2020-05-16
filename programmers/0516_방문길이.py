def solution(dirs):
    x, y = 0, 0
    first = [(0,0)]
    cnt = 1
    direction = ['U', 'D', 'R', 'L']
    near = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # def stop(x,y):
    for d in dirs:
        for i in range(len(direction)):
            if d == direction[i]:
                if -5 < x < 5 and -5 < y < 5:
                    # print(x,y)
                    # print(first)
                    # print(cnt)
                    x += near[i][0]
                    y += near[i][1]
                    if (x,y) == (0,0):
                        cnt -= 1
                    elif (x, y) not in first:
                        first.append((x, y))
                        cnt += 1
                else:
                    continue
    # print(first)

    return cnt


dirs = 'LR'  # ans = 1
# dirs = 'ULURRDLLU'
print(solution(dirs))
