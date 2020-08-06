def solution(skill, skill_trees):
    cnt = 0
    for sk in skill_trees:
        res = ''
        for s in sk:
            if s in skill:
                res += s

        if res == skill:
            cnt += 1
        elif len(res) == 0:
            cnt += 1
        # 'BC'
        elif 0 < len(res) <= len(skill):
            temp = 0
            for r in range(len(res)):
                if res[r] == skill[r]:
                    temp += 1

            if temp == len(res):
                cnt += 1

    # print(cnt)

    return cnt


skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

