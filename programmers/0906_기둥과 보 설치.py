# def solution(n, build_frame):
#     answer = [[]]
#     return answer

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

[[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

total = {}
for x, y, a, b in build_frame:
    print(x, y, a, b)
    # if b == 1:  # 설치
    #     if install(x, y, a, total):
    #         total[(x, y, a)] = 1

    # else:  # 삭제
    #     pass

print(total)

answer = sorted(total, key=lambda x:(x[0], x[1]))
print(answer)
