def solution(N, stages):
    check = []
    total = len(stages)
    for i in range(1, N + 1):
        cnt = stages.count(i)

        if cnt == 0:
            fail = 0
        else:
            fail = cnt / total
        total -= cnt

        check.append((i, fail))

    check = sorted(check, key=lambda x: x[1], reverse=True)
    answer = []
    for a, b in check:
        answer.append(a)

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# 1:1, 2:3, 3:2, 4:1, 5:
# N = 4
# stages = [4, 4, 4, 4, 4]

