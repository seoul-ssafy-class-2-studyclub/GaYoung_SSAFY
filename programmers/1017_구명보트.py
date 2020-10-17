def solution(people, limit):
    people = sorted(people)
    start = 0
    end = len(people) - 1

    cnt = 0
    while True:
        if start >= end:
            break

        if people[start] + people[end] <= limit:
            cnt += 1
            start += 1
            end -= 1
        else:
            end -= 1

    # print(len(people) - cnt)
    return len(people) - cnt

# people = [70, 50, 80, 50]
# limit = 100

people = [70, 80, 50]
limit = 100

print(solution(people, limit))