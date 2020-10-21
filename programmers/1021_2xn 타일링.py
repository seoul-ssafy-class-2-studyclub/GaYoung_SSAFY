def solution(n):
    ls = []
    ls.append(1)
    ls.append(2)

    for i in range(2, n):
        ls.append((ls[-1] + ls[-2]) % 1000000007)

    return ls[-1]