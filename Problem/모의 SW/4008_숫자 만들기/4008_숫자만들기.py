from collections import deque

def permutation(arr, k):
    global q

    if k == N - 1:
        q.append(arr)
        return

    else:
        for i in range(4):
            if operations[i] > 0:
                operations[i] -= 1
                permutation(arr + [i], k + 1)
                operations[i] += 1
    return

for t in range(int(input())):
    N = int(input())

    # ['+', '-', '*', '//']
    operations = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    q = deque()
    permutation([], 0)

    max_result = -100000001
    min_result = 100000001

    for operation in q:
        result = numbers[0]
        for i in range(N - 1):
            if operation[i] == 0:
                result += numbers[i + 1]

            elif operation[i] == 1:
                result -= numbers[i + 1]

            elif operation[i] == 2:
                result *= numbers[i + 1]

            else:
                result = int(result / numbers[i + 1])

        if result > max_result:
            max_result = result

        if result < min_result:
            min_result = result

    print('#{} {}'.format(t + 1, max_result - min_result))