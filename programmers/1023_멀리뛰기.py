n = 4
# n = 3

def solution(n):
    check = [1, 2]
    if n == 1:
        return 1
    elif n == 2:
        return 2

    idx = 0
    while len(check) < n:
        check.append(check[idx] + check[idx+1])
        idx += 1

    return check[-1] % 1234567

print(solution(n))