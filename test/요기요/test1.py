

def solution(A, B, C, D):
    import itertools
    ls = []
    cnt = 0
    result = itertools.permutations([A, B, C, D], 4)
    result = list(result)
    for r in result:
        if r[0] == 0:
            if 0 <= r[1] <= 9:
                if 0 <= r[2] <= 5:
                    if 0 <= r[3] <= 9:
                        if r not in ls:
                            ls.append(r)
        elif r[0] == 1:
            if 0 <= r[1] <= 9:
                if 0 <= r[2] <= 5:
                    if 0 <= r[3] <= 9:
                        if r not in ls:
                            ls.append(r)
        elif r[0] == 2:
            if 0 <= r[1] <= 3:
                if 0 <= r[2] <= 5:
                    if 0 <= r[3] <= 9:
                        if r not in ls:
                            ls.append(r)
        else:
            pass
    return len(ls)
