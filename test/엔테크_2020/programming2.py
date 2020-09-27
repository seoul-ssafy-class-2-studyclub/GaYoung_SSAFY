def solution(N):
    check = [0] * 46
    idx = 1
    while True:
        if idx <= 2:
            check[idx] = idx

        elif idx < 46:
            check[idx] = check[idx-2] + check[idx-1]

        if idx > N:
            return check[N]
        else:
            idx += 1

print(solution(4))

