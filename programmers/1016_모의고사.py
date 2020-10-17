def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0] * 3
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            cnt[0] += 1
        if answers[i] == second[i % len(second)]:
            cnt[1] += 1
        if answers[i] == third[i % len(third)]:
            cnt[2] += 1

    mymax = max(cnt)
    answer = []
    for c in range(len(cnt)):
        if cnt[c] == mymax:
            answer.append(c + 1)

    return answer

# answers = [1,2,3,4,5]
answers = [1,3,2,4,2]
print(solution(answers))