def solution(v):
    answer = []
    v1 = []
    v2 = []
    for i in v:
        if i[0] not in v1:
            v1.append(i[0])
        elif i[0] in v1:
            v1.remove(i[0])
        if i[1] not in v2:
            v2.append(i[1])
        elif i[1] in v2:
            v2.remove(i[1])

    answer = v1 + v2
    return answer
