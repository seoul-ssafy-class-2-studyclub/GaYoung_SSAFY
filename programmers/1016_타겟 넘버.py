from collections import deque

def solution(numbers, target):
    ls = deque([0])
    while numbers:
        x = numbers.pop(0)

        answer = []
        for l in ls:
            answer.append(l+x)
            answer.append(l-x)

        ls = answer

    return ls.count(target)

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))
