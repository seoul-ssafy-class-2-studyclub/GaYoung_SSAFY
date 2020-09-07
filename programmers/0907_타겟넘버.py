from itertools import permutations

def solution(numbers, target):
    answers = [0]
    for number in numbers:
        temp = []
        for answer in answers:
            temp.append(answer + number)
            temp.append(answer - number)

        answers = temp

    cnt = 0
    for i in answers:
        if i == target:
            cnt += 1

    # print(cnt)
    return cnt

numbers = [1, 1, 1, 1, 1]
target = 3

# temp = ['+'] * len(numbers) + ['-'] * len(numbers)
# comb = list(permutations(temp,4))  # 갯수 너무많음
# print(len(comb))


