for t in range(10):
    word1 = ['(', '[', '{', '<']
    word2 = [')', ']', '}', '>']
    N = int(input())
    data = input()
    stack = []
    result = 1

    for i in range(N):
        for j in range(len(word1)):
            if data[i] == word1[j]:
                stack.append(word2[j])
        if stack and data[i] == stack[-1]:
            stack.pop()
        elif data[i] == ')' or data[i] == ']' or data[i] == '}' or data[i] == '>':
            result = 0
            break

    if stack:
        result = 0

    print('#{} {}'.format(t+1, result))