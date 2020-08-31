def solution(N, stages):
    answer = []
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# 1:1, 2:3, 3:2, 4:1, 5:
# N = 4
# stages = [4, 4, 4, 4, 4]

check = []
for i in range(1, N+1):
    cnt = stages.count(i)

    if cnt == 0:
        fail = 0
    else:
        fail = i / cnt
        print(fail)
