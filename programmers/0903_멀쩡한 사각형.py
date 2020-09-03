def maxcommon(a, b):
    mymin = min(a, b)
    answer = 0
    for i in range(mymin, 0, -1):
        if a % i == 0 and b % i == 0:
            answer = i
            break

    return answer

def solution(w,h):

    line = w + h - maxcommon(w, h)
    answer = w * h - line

    return answer

print(solution(8, 12))