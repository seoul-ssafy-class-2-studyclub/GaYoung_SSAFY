for t in range(int(input())):
    data = input()
    stack = []
    result = 1

    for i in range(len(data)):
        if data[i] == '(':
            stack.append(')')
        elif data[i] == '{':
            stack.append('}')
        elif stack and data[i] == stack[-1]:
            stack.pop()
        elif data[i] == ')' or data[i] == '}':
            result = 0
            break
    
    if stack:
        result = 0
    
    print('#{} {}'.format(t+1, result))

# flag 다르게 작성
# for t in range(int(input())):
#     data = input()
#     stack = []
#     flag = 1

#     for i in range(len(data)):
#         if data[i] == '(':
#             stack.append(')')
#         elif data[i] == '{':
#             stack.append('}')
#         elif stack and data[i] == stack[-1]:
#             stack.pop()
#         elif data[i] == ')' or data[i] == '}':
#             flag = 0
#             break
    
#     if stack == [] and flag:
#         result = 1
#     else:
#         result = 0
    
#     print('#{} {}'.format(t+1, result))

# 실패
# for t in range(int(input())):
#     stack = [0] * 100
#     top = -1
#     data = input()

#     correct = True
#     for i in range(len(data)):
#         if data[i] == '(' or data[i] == '{':  # push
#             top += 1
#             stack[top] = data[i]
#         elif data[i] == ')' or data[i] == '}':  # pop
#             if top == -1:
#                 correct = False
#                 break
#             top -= 1

#     if top == -1 and correct:
#         result = 1        
#     else:
#         result = 0
#     print('#{} {}'.format(t + 1, result))