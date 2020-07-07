def solution(s):
    answer = True

    p, y = 0, 0
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1

    if p != y:
        answer = False

    return answer