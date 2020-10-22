def solution(s):
    stack = []

    for i in range(len(s)):
        if s[i] is '(':
            stack.append(i)
        elif s[i] is ')':
            if len(stack) is 0:
                return False
            stack.pop()

    if len(stack) is not 0:
        return False

    return True