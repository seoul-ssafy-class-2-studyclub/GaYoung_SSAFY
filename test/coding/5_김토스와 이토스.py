'''
100 300 10 0 40 0 0 70 65
40 300 20 10 10 20 100 10 0
'''

for i in range(2):
    if i == 0:
        kim = list(map(int, input().split()))
    else:
        lee = list(map(int, input().split()))

answer = [0] * len(kim)
lee_m = 0
for i in range(len(kim)):
    if answer[i-1] > 0:
        lee_m = 0

    money = kim[i] - lee[i]
    if money >= 0:

        if lee_m < 0:
            if money + lee_m >= 0:
                answer[i] = money+lee_m
            else:
                lee_m = money+lee_m
        else:
            answer[i] = money
    else:
        lee_m += money

result = ''
for i in answer:
    result += str(i) + ' '

print(result[:-1])