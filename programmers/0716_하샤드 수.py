def solution(x):
    sum = 0
    for i in str(x):
        sum = int(i) + sum

    if x % sum:
        return False

    return True
