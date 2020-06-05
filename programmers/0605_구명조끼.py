def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people) - 1
    people_cnt = len(people)

    # 최대 2명
    while i < j:

        if people[i] + people[j] <= limit:
            i += 1
            cnt += 1
            j -= 1
        else:
            j -= 1

    return people_cnt - cnt

people = [70, 50, 80, 50]
limit = 100

# people = [70, 80, 50]
# limit = 100

print(solution(people,limit))