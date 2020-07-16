def solution(num):
    i = 0
    while num > 1:
        if num % 2:
            num = num * 3 + 1
        else:
            num / 2
        i += 1

    if i < 500:
        return i
    else:
        return -1
