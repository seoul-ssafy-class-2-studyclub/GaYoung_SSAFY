# 길은 양방향성인 것을 고려하지 않음! -> all 실패,,
# def solution(dirs):
#     x, y = 0, 0
#     first = []
#     cnt = 1
#     direction = ['U', 'D', 'R', 'L']
#     near = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     for d in dirs:
#         for i in range(len(direction)):
#             if d == direction[i]:
#                 if -5 < x < 5 and -5 < y < 5 and (x, y) not in first:
#                     x += near[i][0]
#                     y += near[i][1]
#                 else:
#                     continue
#     # print(first)
#
#     return cnt


dirs = 'ULURRDLLU'
# dirs = 'LULLLLLLU'
# dirs = 'LR'

def solution(dirs):
    direction = ['U','D','R','L']
    near = [(0,1),(0,-1),(1,0),(-1,0)]
    #         U      D     R      L

    x,y = 0,0
    visit = []
    cnt = 0
    for d in dirs:
        for i in range(len(direction)):
            if d == direction[i]:
                xi = x + near[i][0]
                yi = y + near[i][1]
                if -5 <= xi <= 5 and -5 <= yi <= 5:
                    if (x,y,xi,yi) not in visit:
                        # 두개씩 추하가는 이유
                        # (0,0)에서 (0,1)가는거랑 (0,1)에서 (0,0)가는거랑 다르지만 결국 길은 1개이다!!
                        # -> 방향은 단방향이지만, 길은 양방향!!!
                        # (0,0), (0,1)을 지나가는 방법은 2개 (0,0)->(0,1)이랑 (0,1)->(0,0)지나가는 방법
                        # 그런데, 지나간 길 갯수를 세기 위해서는 (0,0)->(0,1)이나 (0,0)->(0,1) 어떤걸 지나가든 상관없이 cnt+=1
                        visit.append((x, y, xi, yi))
                        visit.append((xi, yi, x, y))
                        cnt += 1
                else:
                    continue
                x, y = xi, yi

    print(visit)
    return cnt


print(solution(dirs))
