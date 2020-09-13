from collections import deque

def solution(n):

    n = str(n)
    if len(n) == 1:
        return [0, int(n)]

    def make_number(x, cnt):
        for i in range(len(x) - 1):
            a, b = x[:i + 1], x[i + 1:]
            for j in list(b):
                if j == '0':
                    break

            else:
                numbers.append([str(int(a) + int(b)), cnt + 1])


    numbers = deque([[n, 0]])
    while True:
        if numbers:
            x, cnt = numbers.popleft()
            if len(x) == 1:
                return [cnt, int(x)]

            make_number(x, cnt)


# n = 73425
# n = 10007
n = 9

print(solution(n))
