from itertools import permutations

def solution(numbers):

    # 소수인지 구분
    def check(number):
        if number <= 1:
            return False

        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False

        return True

    numbers = list(numbers)

    # 가능한 숫자들 num_ls에 모으기
    num_ls = []
    for i in range(1, len(numbers) + 1):
        ls = list(permutations(numbers, i))
        for j in ls:
            num = int(''.join(j))
            if num not in num_ls:
                num_ls.append(num)

    # 소수인 것들 갯수 구하기기
    cnt = 0
    for i in num_ls:
        if check(i):
            cnt += 1

    return cnt

# numbers = '17'
numbers = '011'
# print(solution(numbers))


def check(number):
    if number <= 1:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
        return True

print(check(9973))