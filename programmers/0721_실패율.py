# 리스트
def solution(N, stages):
    ans = []

    ln = len(stages)
    for i in range(1, N + 1):
        cnt = stages.count(i)
        if cnt == 0:
            fail = 0
        else:
            fail = cnt / ln
        ans.append((i, fail))
        ln -= cnt
    print(ans)
    ans = sorted(ans, key=lambda x: x[1], reverse=True)
    ans = [i[0] for i in ans]

    return ans

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))
# 딕셔너리
# ans = {}
# for i in range(1, N+1):
#     cnt = stages.count(i)
#     if cnt == 0:
#         fail = 0
#     else:
#         fail = cnt / len(stages)
#     ans[i] = fail
# #??????????????????????????????????????????
# print(ans)
# ans = sorted(ans, key=lambda x: ans[x], reverse=True)
# print(ans)