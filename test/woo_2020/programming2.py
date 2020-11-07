def solution(s, op):
    answer = []
    for i in range(1, len(s)):
        left, right = s[:i], s[i:]
        if op == '+':
            res = int(left) + int(right)
        if op == '-':
            res = int(left) - int(right)
        if op == '*':
            res = int(left) * int(right)
        answer.append(res)
    return answer