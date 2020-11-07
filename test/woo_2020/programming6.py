# logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

logs = ["0001 1 100", "0001 2 100", "0001 3 100", "0001 4 100", "0001 5 100",
        "0003 1 100", "0003 2 100", "0003 3 100", "0003 4 100", "0003 5 100",
        "1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]
# logs = ["1901 10 50", "1909 10 50"]

from collections import defaultdict
from itertools import combinations

def solution(logs):
    res = []
    for i in logs:
        ls = i.split(' ')
        ls[1], ls[2] = int(ls[1]), int(ls[2])
        res.append(ls)
    logs = sorted(res, key=lambda x: (x[0], x[1], x[2]))
    print(logs)
    check = defaultdict(dict)
    for log in logs:
        person, question, score = log
        if person not in check:
            check[person][question] = score
        else:
            check[person][question] = score

    people = []
    for key, val in check.items():
        if len(val) >= 5:
            people.append(key)

    if len(people) <= 1:
        return ["None"]

    answer = []
    result = list(combinations(people, 2))

    for i in result:
        if check[i[0]] == check[i[1]]:
            if i[0] not in answer and i[1] not in answer:
                answer.append(i[0])
                answer.append(i[1])

            elif i[0] in answer and i[1] not in answer:
                answer.append(i[1])

            elif i[1] in answer and i[0] not in answer:
                answer.append(i[0])
    # print(answer)
    return answer

print(solution(logs))