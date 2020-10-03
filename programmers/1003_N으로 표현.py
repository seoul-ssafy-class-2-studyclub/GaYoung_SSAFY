'''
[풀이방법]
1. 우선 5를 1번부터 8번까지 사용할 수 있다(8이 넘으면 return -1)
2. 1번 사용 : 5
   2번 사용 : 55 -> 5를 연속으로 이어 붙인 수
             10, 0, 25, 1 -> 1번 set과 1번 set을 사칙연산
   3번 사용 : 555
             1번 set와 2번 set 사칙연산
             2번 set와 1번 set 사칙연산
'''
# N = 5
# number = 12

def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        num_set = {int(str(N) * i)}

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    num_set.add(x + y)
                    num_set.add(x - y)
                    num_set.add(y - x)
                    num_set.add(x * y)

                    if y != 0:
                        num_set.add(x // y)

                    if x != 0:
                        num_set.add(y // x)

        if number in num_set:
            return i

        DP.append(num_set)

    return answer


N = 1
number = 1111
print(solution(N, number))
