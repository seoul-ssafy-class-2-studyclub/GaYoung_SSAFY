from itertools import permutations

def solution(numbers):
    numbers = list(numbers)

    def check(number):
        if number <= 1:
            return False

        for i in range(2, number // 2 + 1):
            # i를 숫자의 반만 돌리기 때문에 그 사이에 0으로 나누어 떨어지는 값이 있으면 소수가 아니다
            if number % i == 0:
                return False

        return True

    total = []
    for i in range(1, len(numbers) + 1):
        res = list(permutations(numbers, i))
        print(res)
        for r in res:
            num = int(''.join(r))
            if num not in total:
                total.append(num)
    print(total)

    cnt = 0
    for tot in total:
        print(check(tot))
        if check(tot):
            cnt += 1

    # print(cnt)

    return cnt

# numbers = '17'
numbers = '011'

print(solution(numbers))