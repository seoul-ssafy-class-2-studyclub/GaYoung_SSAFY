# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# numbers = list(map(int, input().split()))
user_input = 7
numbers = ['7','6','5','2','3','1','4']

def merge_split(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    left = merge_split(left)
    right = merge_split(right)

    # 하나하나 다 쪼개기
    # 쪼갠 것을 다시 붙이기
    return merge_join(left, right)


def merge_join(left, right):
    answer = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                answer.append(left[0])
                left = left[1:]
            else:
                answer.append(right[0])
                right = right[1:]

        elif len(left) > 0:
            answer.append(left[0])
            left = left[1:]

        elif len(right) > 0:
            answer.append(right[0])
            right = right[1:]

    return ' '.join(answer)


print(merge_split(numbers))