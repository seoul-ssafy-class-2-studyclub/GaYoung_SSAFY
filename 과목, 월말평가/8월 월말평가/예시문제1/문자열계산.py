# def calc(equation):
#     x = 0
#     y = ''
#     if equation[0].isdigit():
#         equation = '+' + equation
#     for num in equation[::-1]:
#         if num == '+':
#             x += int(y)
#             y = ''
#         elif num == '-':
#             x -= int(y)
#             y = ''
#         else:
#             y = num + y
#     return x

data = '123+2-124'
print(data.isdigit())