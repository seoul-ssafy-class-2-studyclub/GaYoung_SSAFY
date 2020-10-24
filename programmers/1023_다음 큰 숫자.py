n = 78
# n = 15


def solution(n):

    # print(type(bin(n)[2:]))
    one_cnt = bin(n)[2:].count('1')

    for i in range(n+1, 1000001):
        if bin(i).count('1') == one_cnt:
            return i
