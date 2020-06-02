import itertools

def check(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True


def solution(numbers):
    numbers = list(numbers)   # numb = [i for i in numbers]과 동일!!

    ans = 0
    possible = []
    for n in range(1, len(numbers)+1):
        res = list(map(''.join, itertools.permutations(list(numbers), n)))
        # print(res)
        for r in res: # 011과 11은 동일! -> 중복 제거를 위해
            r = int(r)
            if r not in possible and r != 0:
                possible.append(int(r))
    # print(possible)


    for poss in possible:
        print(check(poss))
        if check(poss):
            ans += 1

    # print(ans)

    return ans

numbers = '17'
# numbers = '011'

print(solution(numbers))