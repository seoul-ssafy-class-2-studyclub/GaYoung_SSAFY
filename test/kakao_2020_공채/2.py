from itertools import combinations

def solution(orders, course):
    answer = []
    return answer

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

# orders = ["XYZ", "XWY", "WXA"]
# course = [2, 3, 4]

orders_data = []
for i in orders:
    i = sorted(i)
    orders_data.append(list(i))

answer = []
for i in course:
    data = {}
    for order in orders_data:
        if len(order) >= i:
            comb = list(combinations(order, i))
            for j in comb:
                if j not in data:
                    data[j] = 1
                else:
                    data[j] += 1

    mymax = 0
    for value in data.values():
        if value > mymax:
            mymax = value

    for key, value in data.items():
        if mymax >= 2 and mymax == value:
            answer.append(''.join(key))

print(sorted(answer))
