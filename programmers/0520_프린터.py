def solution(priorities, location):
    ls = [(priorities[p], p) for p in range(len(priorities))]
    # [(0, 2), (1, 1), (2, 3), (3, 2)]

    wait = []
    while len(ls) != 0:
        if ls[0][0] == max(ls)[0]:  # 중요도가 가장 높으면
            wait.append(ls.pop(0))  # 인쇄한걸 바로 wait에 저장
            # print(wait)
        else:  # 중요도가 가장 높지 않은경우
            ls.append(ls.pop(0))  # 문서를 대기목록 맨 뒤로 보낸다

    for w in range(len(wait)):
        if wait[w][1] == location:
            return w+1

priorities = [1,2,3,4]
location =2


res = solution(priorities, location)
print(res)