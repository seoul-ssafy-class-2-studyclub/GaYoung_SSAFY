def solution(people, limit):
    # 최대 2명씩 탄다.
    people = sorted(people)  # [40, 50, 60, 80]
    i = 0
    j = len(people) - 1

    cnt = 0
    while i < j:
        if people[i] + people[j] <= limit:
            cnt += 1
            i += 1
            j -= 1
        else:
            j -= 1

    return len(people) - cnt

# people = [70, 50, 80, 50]
# limit = 100

people = [60, 40, 80, 50]
limit = 110

# people = [70, 80, 50]
# limit = 100

def solution_for(people, limit):  # 정확성 O, 효율성 X(시간초과)
    people = sorted(people)  # [40, 50, 60, 80]
    i = 0
    j = len(people) - 1

    cnt = 0
    visit = [0] * len(people)
    for i in range(len(people)):
        if visit[i] == 0:
            for j in range(len(people) - 1, i, -1):
                if visit[j] == 0:
                    if people[i] + people[j] <= limit:
                        visit[i], visit[j] = 1, 1
                        cnt += 1
                    else:

                        continue
                    break

    for i in visit:
        if i == 0:
            cnt += 1

    return cnt
