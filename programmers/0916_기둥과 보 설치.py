def install(x, y, a, total):
    if a == 0:  # 기둥
        if y == 0:  # 바닥 위에 있거나
            return True
        if (x - 1, y, 1) in total or (x, y, 1) in total:  # 보의 한쪽 끝 부분 위에 있거나
            return True
        if (x, y - 1, 0) in total:  # 다른 기둥 위에 있으면
            return True
        else:
            return False

    else:  # 보
        if y == 0:
            return False
        if (x, y - 1, 0) in total or (x + 1, y - 1, 0) in total:  # 한쪽 끝 부분이 기둥 위에 있거나
            return True
        if (x - 1, y, 1) in total and (x + 1, y, 1) in total:  # 양쪽 끝 부분이 다른 보와 동시에 연결
            return True
        else:
            return False



def solution(n, build_frame):
    # 원래 total = []하려했는데, pop할때 특정짓기 힘들어서 {}로 수정
    total = {}
    # 8방향으로 하는 이유 : install함수에서 x-1, x+1, y-1, y+1과 같이 비교해야하는 부분들이 있기 때문에
    near = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (0, 0)]
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if install(x, y, a, total):
                total[x, y, a] = 1

        else:  # 삭제 -> install의 결과가 False가 되어야함
            # if (x, y, a) in total:  # 이걸 확인해야하는 것이 아니라 xi, yi값이 total에 있는지 확인해야한다.
            total.pop((x, y, a))

            for dx, dy in near:
                xi, yi = x + dx, y + dy
                if (xi, yi, 0) in total:
                    if not install(xi, yi, 0, total):
                        total[x, y, a] = 1  # 이때, total[xi, yi, a] = 1이 아니다.
                        break

                if (xi, yi, 1) in total:
                    if not install(xi, yi, 1, total):
                        total[x, y, a] = 1  # 이때, total[xi, yi, a] = 1이 아니다.
                        break

    # print(total)
    answer = list(map(list, total.keys()))
    answer = sorted(answer)  # [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]
    # print(answer)

    return answer

# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))