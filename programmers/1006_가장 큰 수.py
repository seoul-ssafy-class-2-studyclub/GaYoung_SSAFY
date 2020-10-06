# numbers = [3, 30, 34, 5, 9]
# numbers = [6, 10, 2]
numbers = [1, 12, 123, 1000]
# numbers = [0, 0, 0, 0]

'''
1    -> 111111111111
12   -> 121212121212
123  -> 123123123123
1000 -> 100010001000
답 : 123/12/1/1000
1,2,3,4최소공배수=12 -> 12자리로 맞추고 큰값 비교
'''

def solution(numbers):
    numbers = [str(i) for i in numbers]

    if ''.join(numbers) == '0' * len(numbers):
        return '0'

    temp = []
    for number in numbers:

        if len(number) == 1:
            temp.append([number * 12, number])

        elif len(number) == 2:
            temp.append([number * 6, number])

        elif len(number) == 3:
            temp.append([number * 4, number])

        elif len(number) == 4:
            temp.append([number * 3, number])

    temp = sorted(temp, reverse=True)

    answer = ''
    for x, y in temp:
        answer += y

    return answer

print(solution(numbers))