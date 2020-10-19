# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def make(x, y, type, total):
    if type == 0:  # 0: 기둥
        if y == 0:  # 기둥은 바닥 위에 있거나
            return True
        if (x - 1, y, 1) in total or (x, y, 1) in total:  # 보의 한쪽 끝 부분 위에 있거나
            return True
        if (x, y - 1, 0) in total:  # 다른 기둥 위에 있으면
            return True
        else:
            return False

    elif type == 1:  # 1: 보
        if y == 0:
            return False
        if (x, y - 1, 0) in total or (x + 1, y - 1, 0) in total:  # 보는 한쪽 끝 부분이 기둥 위에 있거나,
            return True
        if (x - 1, y, 1) in total and (x + 1, y, 1) in total :  # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야
            return True
        else:
            return False

def solution(n, build_frame):
    total = {}
    near = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (0, 0)]
    for x, y, type, install in build_frame:
        if install == 1:  # 1: 설치
            if make(x, y, type, total):
                total[x, y, type] = 1

        elif install == 0:  # 0: 삭제
            total.pop((x, y, type))
            for a, b in near:
                xi, yi, = x + a, y + b
                if (xi, yi, 0) in total:
                    if not make(xi, yi, 0, total):
                        total[x, y, type] = 1  # 이때, total[xi, yi, a] = 1이 아니다.
                        break

                if (xi, yi, 1) in total:
                    if not make(xi, yi, 1, total):
                        total[x, y, type] = 1  # 이때, total[xi, yi, a] = 1이 아니다.
                        break

    total = sorted(total.keys())
    # print(total)

    return total