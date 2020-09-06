def solution(brown, yellow):
    total = brown + yellow
    possible = []
    for i in range(total, 2, -1):
        if total % i == 0 and i >= total // i:
            possible.append([i, total // i])

    for i in possible:
        if (i[0] - 2) * (i[1] - 2) == yellow:
            return i

brown, yellow = 10, 2
# brown, yellow = 8, 1
# brown, yellow = 24, 24

