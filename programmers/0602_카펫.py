brown = 10
yellow = 2

# brown = 8
# yellow = 1

# brown = 24
# yellow = 24

def solution(brown, yellow):

    total = brown + yellow
    possible = []
    for i in range(total, 2,-1):
        if total % i == 0 and i >= total // i:
            possible.append([i, total // i])
    # print(possible)

    for poss in possible:
        check = (poss[0] - 2) * (poss[1] - 2)
        if check == yellow:
            return poss

print(solution(brown,yellow))