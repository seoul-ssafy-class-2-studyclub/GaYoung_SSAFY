skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):

    cnt = 0
    for i in skill_trees:
        temp = ''
        for j in i:
            if j in skill:
                temp += j

        if temp == skill:
            cnt += 1

        elif len(temp) < len(skill):
            if temp == skill[:len(temp)]:
                cnt += 1

    # print(cnt)
    return cnt