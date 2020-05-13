import itertools

# def solution(expression):
expression = "50*6-3*2"
answer = 0
comp = []
numb = []
for i in expression:
    if i == "*" or i == "-" or i == "+":
        if i not in comp:
            comp.append(i)
        numb.append(i)
    else:
        numb.append(int(i))

    can = list(itertools.permutations(comp, len(comp)))

print(numb)

# for i in range(len(numb)):
#     for j in range(i,len(numb)):
#         for c in comp:
#             if c not in expression[i:j]:
#                 new.append(expression[i:j])
#
# print(new)

    # return answer