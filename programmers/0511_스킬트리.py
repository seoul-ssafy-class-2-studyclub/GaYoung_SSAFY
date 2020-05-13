def solution(skill, skill_trees):
    cnt = 0
    for sk in skill_trees:
        res = ''
        res_cnt = 0
        for s in sk:
            if s in skill:
                res += s
        # print(res)

        if res == skill:
            cnt += 1
        elif len(res) == 0:
            cnt += 1
        elif 0 < len(res) <= len(skill):
            for i in range(len(res)):
                if res[i] == skill[i]:
                    res_cnt += 1
            if res_cnt == len(res):
                cnt += 1
    # print(cnt)
    #
    # print('------------------------------------')
    return cnt
#     return answer


skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
ans = solution(skill, skill_trees)
print(ans)