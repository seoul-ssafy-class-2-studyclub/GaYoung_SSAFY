def solution(p):
    res = ''
    while True:
        p += 1
        check = []
        for i in str(p):
            if i in check:
                continue
            else:
                check.append(i)
        # print(check)
        if len(check) == 4:
            res = ''.join(check)
            # print(int(res))
            break

    return int(res)

print(solution(1987))
p = 1987
# p = 2015



