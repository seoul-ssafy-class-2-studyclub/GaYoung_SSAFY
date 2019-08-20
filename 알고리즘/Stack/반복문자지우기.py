for t in range(int(input())):
    data = list(input())
    stack = []
    for i in range(len(data)):
        if not stack or data[i] != stack[-1]: 
            stack.append(data[i])
        elif stack and data[i] == stack[-1]:
            stack.pop()

    print('#{} {}'.format(t + 1, len(stack)))