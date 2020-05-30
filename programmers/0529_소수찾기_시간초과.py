import itertools

def check(number):
    cnt = 0
    for i in range(1, number+1):
        if number % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    return False

def solution(numbers):
    numbers = list(numbers)   # numb = [i for i in numbers]과 동일!!

    ans = 0
    possible = []
    for n in range(1, len(numbers)+1):
        res = list(map(''.join, itertools.permutations(list(numbers), n)))
        # print(res)
        for r in res: # 011과 11은 동일! -> 중복 제거를 위해
            r = int(r)
            if r not in possible:
                possible.append(int(r))

    for po in possible:
        if check(po):
            ans += 1

    return ans

# numbers = '17'
numbers = '011'

print(solution(numbers))