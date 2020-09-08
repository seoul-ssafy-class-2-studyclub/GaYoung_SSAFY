# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def install(x, y, a, total):
    if a == 0:  # 기둥
        if y == 0:  # 바닥 위
            return True
        if (x, y, 1) in total or (x - 1, y, 1) in total:  # 보의 한쪽 끝 부분 위
            return True
        if (x, y - 1, 0) in total:  # 다른 기둥 위
            return True
        else:
            return False

    else:   # 보
        if y == 0:
            return False
        if (x, y - 1, 0) in total or (x + 1, y - 1, 0) in total:  # 한쪽 끝 부분이 기둥 위
            return True
        if (x - 1, y, 1) in total and (x + 1, y, 1) in total:  # 양쪽 끝 부분이 다른 보와 동시에 연결
            return True
        else:
            return False


def solution(n, build_frame):
    total = {}
    n += 1
    near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # near = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (0, 0)]
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if install(x, y, a, total):
                total[(x, y, a)] = 1
                # total[[x, y, a]] = 1 -> TypeError: unhashable type: 'list'

        else:  # 삭제
            if (x, y, a) in total:
                total.pop((x, y, a))  # 원래 total = []하려했는데, pop할때 특정짓기 힘들어서 {}로 수정
                for dx, dy in near:
                    xi, yi = x + dx, y + dy
                    if (xi, yi, a) in total:
                        if (xi, yi, a) in total:
                            if not install(xi, yi, a, total):
                                total[(x, y, a)] = 1
                                break

    total = list(map(list, total.keys()))
    answer = sorted(total, key=lambda x: (x[0], x[1]))

    return answer

print(solution(n, build_frame))