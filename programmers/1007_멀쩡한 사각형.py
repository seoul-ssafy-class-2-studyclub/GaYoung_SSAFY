from math import gcd

def solution(w,h):
    line = w + h - gcd(w, h)
    answer = w * h - line
    return answer