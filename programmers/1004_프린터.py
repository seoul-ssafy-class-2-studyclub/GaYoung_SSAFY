# priorities = [2, 1, 3, 2]
# location = 2

priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):

    ls = []
    for i in range(len(priorities)):
        ls.append([priorities[i], i])

    cnt = 0
    while ls:

        mymax = max(ls)[0]
        val, idx = ls.pop(0)  # 미리 빼버리면 val 이랑 max(ls)[0]비교할 때

        if val == mymax:
            cnt += 1

            if location == idx:
                return cnt

        else:
            ls.append([val, idx])

print(solution(priorities, location))