def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            correct[0] += 1
        if answers[i] == second[i % len(second)]:
            correct[1] += 1
        if answers[i] == third[i % len(third)]:
            correct[2] += 1

        print(correct)

    ans = []
    mymax = max(correct)
    for c in range(len(correct)):
        if correct[c] == mymax:
            ans.append(c + 1)

    return ans

answers = [1,3,2,4,2]
print(solution(answers))
