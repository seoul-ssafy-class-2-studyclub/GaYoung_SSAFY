from itertools import permutations

def check(num):
    if num <= 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    cnt = []
    for i in range(1, len(numbers)+1):
        for j in list(permutations(numbers, i)):
            result = int(''.join(j))
            if check(result) and result not in cnt:
                cnt.append(result)
    # print(cnt)
    return len(cnt)

print(solution(numbers='17'))