from itertools import combinations

def part(res, i):
    check = []
    start = 0
    for j in range(2, len(res) + 1, 2):
        temp = res[start:j]
        start = j
        if temp[0] != temp[1]:
            check.append(set(temp))
    if len(check) == i // 2:
        val = check[0]
        for idx in range(1, len(check)):
            val = val & check[idx]

        if len(val) >= 1:
            return True


def solution(a):
    if a == [0]:
        return 0

    n = len(a)
    if n % 2 == 1:  # 홀수
        for i in range(n - 1, 1, -2):
            result = combinations(a, i)
            for res in result:
                if part(res, i):
                    return i

    else:  # 짝수
        for i in range(n, 1, -2):
            result = combinations(a, i)
            for res in result:
                if part(res, i):
                    return i

    return 0

# a = [5,2,3,3,5,3]  # 4
# a = [0,3,3,0,7,2,0,2,2,0]  # 8
# a = [0,0,0,2,3,4,3,5,3,1]  # 6
# a = [4,0,0,2,1,1,1,1,1,1,1,1,0,3] # 6
a = [1,2,2,1,3]  # 4

print(solution(a))
