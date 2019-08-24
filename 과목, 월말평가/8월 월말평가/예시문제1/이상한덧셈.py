# # def calc(equation):
# equation = '123+2-124'
# operator = ['+', '-']
# index_1 = 0
# numbers = []
# for i in range(len(equation)):
#     if equation[i] in operator and i != 0:
#         index_2 = i
#         numbers.append(equation[index_1:index_2])
#         index_1 = index_2
#     # if i == len(equation) - 1
# numbers.append(equation[index_1:])
# print(numbers)

# result = sum(list(map(int, numbers)))
# return result


# def calc(equation):
#     operator = ['+', '-']
#     index_1 = 0
#     numbers = []
#     for i in range(len(equation)):
#         if equation[i] in operator:
#             index_2 = i
#             numbers.append(equation[index_1:index_2])

a = '123'
b = '+2'
c = '-333'
A = int(a)
B = int(b)
C = int(c)
print(sum([A, B, C]))